from django.shortcuts import render,redirect
#from .models import Profile
from django.contrib.auth.decorators import login_required
from .email import send_welcome_email
from django.http import HttpResponse, Http404,HttpResponseRedirect
from .forms import NewsLetterForm
import datetime as dt

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    '''
    '''
    return  HttpResponseRedirect('home')

@login_required(login_url='/accounts/login/')
def home(request):
    date = dt.date.today()
    #instag = Profile.todays_posts()
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
    return render(request, 'home.html',  {"date": date,"letterForm":form})

@login_required
def posts(request):
    date = dt.date.today()
    return render(request, 'all-pages/posts.html', {'date':date})    

@login_required
def pastposts(request, past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(posts)

    return render(request, 'all-pages/pastposts.html', {'date':date,})    


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



