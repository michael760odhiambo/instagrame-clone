from django.db import models

class Comment(models.Model):
     author = models.CharField(max_length=60)
     body = models.TextField()
     created_on = models.DateTimeField(auto_now_add=True)
    


class Like(models.Model):
    like = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    photo = models.ImageField(upload_to='media')
    bio = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)


# class Image(models.Model):
#     profile = models.ForeignKey(Profile)
#     comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
#     like = models.ForeignKey(Like)    