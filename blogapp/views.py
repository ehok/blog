from django.shortcuts import render
from django.utils import timezone
from .models import Post, Comments
from .forms import PostForm
from django.shortcuts import redirect
from Crypto.Cipher import DES
from collections import OrderedDict
import numpy as np
import math as m
import sys
import string

# LETTERS = ['a', 'A', 'b', 'B', 'c', 'C', 'd', 'D', 'e', 'E', 'f', 'F', 'g', 'G', 'h', 'H', 'i', 'I', 'j', 'J', 'k', 'K', 'l', 'L', 'm', 'M', 'n', 'N', 'o', 'O', 'p', 'P', 'q', 'Q', 'r', 'R', 's', 'S', 't', 'T', 'u', 'U', 'v', 'V', 'w', 'W', 'x', 'X', 'y', 'Y', 'z', 'Z']
LETTER_COUNTS = OrderedDict()

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    for post in posts:
        id = post.id
        plaintext = post.plaintext
        key = post.key
        cipher_text = encrypt(plaintext, key)
        decrypted_text = decrypt(cipher_text, key)
        post.ciphertext = cipher_text
        post.decrypted = decrypted_text
        post.save()
    return render(request, 'blog/post_list.html', {'posts': posts})

def comment_list(request):
    random_text = random_generator(1000)
    frequencyOfLetter = get_frequency_analysis(random_text)
    random = Comments.objects.create(random_text=random_text, frequencyOfLetter=frequencyOfLetter, published_date=timezone.now())
    random.save()

    comments = Comments.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/comment_list.html', {'comments': comments})

def post_new(request):
    if request.method == "POST" and "save" in request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            #plaintext = request.POST["plaintext"]
            #key = request.POST["key"]
            #cipher_text = encrypt(plaintext, key)
            #decrypted_text = decrypt(cipher_text, key)
            #post = form.save(commit=False)
            #post.title = request.POST["title"]
            #post.text = ""
            #post.plaintext = plaintext
            #post.ciphertext = cipher_text
            #post.decrypted = decrypted_text
            #post.author = request.user
            #post.published_date = timezone.now()
            #post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def padding(text:str):
    temp = len(bytes(text,"utf8")) % 8
    if temp != 0:
        for i in range(8 - temp):
            text += '~'
    return text
        
def unpadding(text:str):
    return text.replace('~','')

def encrypt(plaintext:str, key:str):
    des = DES.new(key, DES.MODE_ECB)
    plaintext_text = bytes(padding(plaintext), "utf8")
    cipher_text = des.encrypt(plaintext_text)
    return cipher_text

def decrypt(cipher_text:str, key:str):
    des = DES.new(key, DES.MODE_ECB)
    plaintext = des.decrypt(cipher_text)
    return unpadding(plaintext.decode("utf-8"))

def random_generator(text_len:int) -> str:
    """Generates string from random letters with provided length by text_len.
    
    Args:
    text_len: (int) Number of letters.

    Returns:
    (str) Generated random string.
    """
    global LETTER_COUNTS
    LETTER_COUNTS = OrderedDict((letter,0) for letter in string.ascii_letters)
    random_string = list()

    for _ in range(text_len):
        random_letter = string.ascii_letters[np.random.randint(low=0, high=len(LETTER_COUNTS))]
        random_string.append(random_letter)
        LETTER_COUNTS[random_letter] += 1 
    
    return "".join(random_string)


def get_frequency_analysis(random_text:str):
    global LETTER_COUNTS 
    result = ""
    for letter, letter_count in LETTER_COUNTS.items():
        result += str(letter) + ":" + str(letter_count) + " "

    result += "\nLength of Random Text  : " + str(len(random_text)) + "\n"
    result += f"Standat deviation of random letters {np.std(list(LETTER_COUNTS.values()))}"
    return result

    