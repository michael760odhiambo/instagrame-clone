from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.home, name='home'),
    url('^posts/', views.posts, name='posts'),
    url('^pastposts/', views.pastposts, name='pastposts'),
]