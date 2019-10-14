# from django.db import models
# from django.contrib.auth.models import User
# from PIL import Image

# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     title = models.CharField(max_length=30)
#     image = models.ImageField(upload_to='media/')
#     bio = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.user.username} Profile'

#     def save(self):
#             super().save()

#    # img = Image.open(self.image.path)

#     # if img.height > 300 or img.width > 300:
#     #     output_size = (300, 300)
#     #     img.thumbnail(output_size)
#     #     img.save(self.image.path)    

#     @classmethod
#     def todays_posts(cls):
#         today = dt.date.today()
#         instag = cls.objects.filter(created_on=today)
#         return instag    

#     @classmethod
#     def search_by_title(cls,search_term):
#         instag = cls.objects.filter(title__icontains=search_term)
#         return instag    







   
# Create your models here.
