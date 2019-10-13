from django.db import models
import datetime as dt

class Comment(models.Model):
    post = models.ForeignKey('instag.Profile', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
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


class Profile(models.Model):
    title = models.CharField(max_length=30)
    photo = models.ImageField(upload_to='media/')
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title)

    @classmethod
    def todays_posts(cls):
        today = dt.date.today()
        instag = cls.objects.filter(created_on=today)
        return instag    

    @classmethod
    def search_by_title(cls,search_term):
        instag = cls.objects.filter(title__icontains=search_term)
        return instag    


class Image(models.Model):
    profile = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.ForeignKey(Like) 

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()       