from django.contrib import admin
from .models import  Pic,Profile,Follow, Unfollow, Likes,Comment

# Register your models here.

admin.site.register(Pic)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Follow)
admin.site.register(Unfollow)
admin.site.register(Likes)
# Register your models here.
