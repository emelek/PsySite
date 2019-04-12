from django.shortcuts import render

# Create your views here.

def index(request):
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1
    username = request.session['username']
    return render(request, 'user/views.html',{'num_visits':num_visits, 'username': username})