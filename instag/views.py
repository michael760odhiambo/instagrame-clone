from django.shortcuts import render
import datetime as dt

def home(request):
    return render(request, 'home.html')

def posts(request):
    date = dt.date.today()
    return render(request, 'all-pages/posts.html', {'date':date})    

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

    return render(request, 'all-pages/pastposts.html', {'date':date})    

# Create your views here.
