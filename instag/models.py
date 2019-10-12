from django.db import models

class Comment(models.Model):
     author = models.CharField(max_length=60)
     body = models.TextField()
     created_on = models.DateTimeField(auto_now_add=True)
    
     def __str__(self):
        return str(self.author)

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
    def search_by_title(cls,search_term):
        instag = cls.objects.filter(title__icontains=search_term)
        return instag    


class Image(models.Model):
    profile = models.ForeignKey(Profile)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    like = models.ForeignKey(Like) 

       