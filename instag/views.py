from django.shortcuts import render,redirect
import datetime as dt
from .models import Profile

def home(request):
    return render(request, 'home.html')

def posts(request):
    date = dt.date.today()
    return render(request, 'all-pages/posts.html', {'date':date})    

def pastposts(request,past_date):
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(posts)

    return render(request, 'all-pages/pastposts.html', {'date':date})    


def search_results(request):
    
    if 'profile' in request.GET and request.GET["profile"]:
        search_term = request.GET.get("profile")
        searched_profile = Profile.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'all-pages/search.html',{"message":message,"profile": searched_profile})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pages/search.html',{"message":message})

# Create your views here.
