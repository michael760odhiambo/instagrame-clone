from django.contrib import admin
from .models import Profile,Image,Like,Comment

admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Image)
admin.site.register(Comment)

# Register your models here.
