from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    key = models.CharField(max_length=500,default='')
    plaintext = models.TextField(null=True)
    ciphertext = models.TextField(null=True)
    decrypted = models.TextField(null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

class Comments(models.Model):
    random_text = models.TextField()
    frequencyOfLetter = models.TextField()
    published_date = models.DateTimeField(
            blank=True, null=True)

    #def __str__(self):
    #    return self.text


class Signatures(models.Model):
    text = models.TextField(null=True)
    daVinciPrivKey = models.TextField(null=True)
    daVinciPubKey = models.TextField(null=True)
    bobRossPrivKey = models.TextField(null=True)
    bobRossPubKey = models.TextField(null=True)
    decryptedText_daVinci = models.TextField(null=True)
    decryptedText_bobRoss = models.TextField(null=True)
    published_date = models.DateTimeField(
            blank=True, null=True)