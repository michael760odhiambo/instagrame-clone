from django.db import models
import datetime as dt
from django.contrib.auth.models import User
#from annoying.fields import AutoOneToOneField

class Comment(models.Model):
    #post = models.ForeignKey('instag.Profile', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(User, max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class Like(models.Model):
    like = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.like)




class Image(models.Model):
    #profile = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.ForeignKey(Like) 

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()       