from django.shortcuts import render
import datetime as dt

def home(request):
    return render(request, 'home.html')

def posts(request):
    date = dt.date.today()
    return render(request, 'all-pages/posts.html', {'date':date})    

def pastposts(request):
    date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    return render(request, 'all-pages/pastposts.html', {'date':date})    

# Create your views here.
