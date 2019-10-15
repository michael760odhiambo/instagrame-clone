from django.shortcuts import render,redirect
from .models import Profile
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewsLetterForm,CommentForm
import datetime as dt
from .models import Comment

Post = Profile

@login_required(login_url='/accounts/login/')
def profile(request):
    '''
    '''
    context = {
        'posts':Profile.objects.all()
    }
    return  render(request,'all-pages/profile.html',context)

class PostListView(ListView):
    model = Post
    template_name = 'home.html' 
    context_object_name = 'posts'
    ordering = ['-created_on']


class PostDetailView(DetailView):
    model = Post
    template_name = 'all-pages/post_detail1.html'


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'bio','photo']
    template_name = 'all-pages/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'bio']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    instag = Profile.todays_posts()
    form = NewsLetterForm() 
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']
            email = form.cleaned_data['email']
            recipient = NewsLetterRecipients(name = name,email =email)
            recipient.save()

            send_welcome_email(name,email)

            HttpResponseRedirect('home')
    else:
         form = NewsLetterForm()
    return render(request, 'home.html',  {"date": date,"instag":instag,"letterForm":form})

@login_required
def posts(request):
    date = dt.date.today()
    return render(request, 'all-pages/posts.html', {'date':date})    



@login_required
def search_results(request):
    
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pages/search.html',{"message":message,"profile": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pages/search.html',{"message":message})


def signup(request):
    HttpResponseRedirect (request,'accounts/registration_form.html')


@login_required(login_url='/accounts/login/')
def comments(request):

    if request.method != 'POST':

        form = CommentForm()
    else:
        # Comment posted
        form = CommentForm(data=request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = request.user
            new_comment.profile = profile
            form.save()
            return HttpResponseRedirect(reverse('instag:profile'))    
    '''
    '''
    context = {
        'comments':Comment.objects.all()
    }
    return  render(request,'all-pages/comments.html',context)



