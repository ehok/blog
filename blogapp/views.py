from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from Crypto.Cipher import DES
import sys


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST" and "save" in request.POST:
        form = PostForm(request.POST)
        if form.is_valid():
            plaintext = request.POST["text"]
            key = request.POST["key"]
            cipher_text = encrypt(plaintext, key)
            post = form.save(commit=False)
            post.title = request.POST["title"]
            post.text = plaintext + '|' + str(cipher_text)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_list')
    #elif request.method == "POST" and "decode_btn" in request.POST:
    #    form = PostForm(request.POST)
    #    if form.is_valid():
    #        des = DES.new('01234567', DES.MODE_ECB)
    #        id = form.cleaned_data['text']
    #        cipher_text = Post.objects.get(id=id)
    #        print(cipher_text.text)
    #        plaintext = des.decrypt(cipher_text.text)
    #        post = form.save(commit=False)
    #        post.title = cipher_text.title
    #        post.text = unpadding(str(plaintext))
    #        post.author = request.user
    #        post.published_date = timezone.now()
    #        post.save()
    #        return redirect('post_list')
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
    cipher_text = des.encrypt(padding(plaintext))
    return cipher_text

def decrypt(cipher_text:str, key:str):
    des = DES.new(key, DES.MODE_ECB)
    plaintext = des.decrypt(cipher_text.text)
    return unpadding(plaintext)