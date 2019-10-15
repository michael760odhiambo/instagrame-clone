from django.conf.urls import url
from . import views
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #url('^$', views.home, name='home'),
    url('^posts/', views.posts, name='posts'),
    url('^profile/', views.profile, name='profile'),
    url('^comments/', views.comments, name='comments'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^$', PostListView.as_view(), name='home'),
    url('post/(?P<pk>\d+)/', PostDetailView.as_view(), name='post-detail'),
    url('post/new/', PostCreateView.as_view(), name='post-create'),
    url('post/(?P<pk>\d+)/update/', PostUpdateView.as_view(), name='post-update'),
    url('post/(?P<pk>\d+)/delete/', PostDeleteView.as_view(), name='post-delete'),
    #url('about/', views.about, name='about'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
