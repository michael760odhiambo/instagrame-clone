from django.db import models
import datetime as dt
from django.contrib.auth.models import User
from django.urls import reverse
#from tinymce.models import HTMLField

#from django.conf import settings

class Pic(models.Model):
    pic = models.ImageField(upload_to='media')
    user = models.ForeignKey(User, null=True)
    pic_name = models.CharField(max_length=30,null=True)
    likes = models.IntegerField(default=0)
    pic_caption = models.TextField(null=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.pic_name

    def delete_pic(self):
        self.delete()

    def save_pic(self):
        self.save()

    def update_caption(self, new_caption):
        self.pic_caption = new_caption
        self.save()
    @classmethod
    def get_pics_by_user(cls,id):
        sent_pics = Pic.objects.filter(user_id=id)
        return sent_pics

    @classmethod
    def get_pic_by_id(cls, id):
        fetched_pic = Pic.objects.get(id=id)
        return fetched_pic

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return str(self.user.username)

    def save_profile(self):
        self.save()

class Profile(models.Model):
    username = models.CharField(default='User', max_length=30)
    profile_pic = models.ImageField(upload_to='media/', null=True)
    bio = models.TextField(default='', blank=True)
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)

    def __str__(self):
        return str(self.username)

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save()

    @classmethod
    def search_profile(cls, search_term):
        got_profiles = cls.objects.filter(first_name__icontains=search_term) 
        return got_profiles           

class Comment(models.Model):
    user = models.ForeignKey(User, null= True)
    pic = models.ForeignKey(Pic, null= True, related_name='comment')
    comment= models.TextField( blank=True)

    def __str__(self):
	    return str(self.comment)

    def delete_comment(self):
        self.delete()

    def save_comment(self):
        self.save()
class Follow(models.Model):
    user = models.ForeignKey(Profile, null=True)
    follower = models.ForeignKey(User, null=True)

    def __str__(self):
        return str(self.follower)

    def save_follower(self):
        self.save()

    def delete_follower(self):
        self.save()

class Unfollow(models.Model):
    user = models.ForeignKey(Profile,null=True)
    follower = models.ForeignKey(User, null=True)

    def __str__(self):
    	return str(self.name)

class Likes(models.Model):
    user = models.ForeignKey(Profile, null=True)

    def __int__(self):
        return (self.name)

    def unlike(self):
        self.delete()

    def save_like(self):
        self.save()







































