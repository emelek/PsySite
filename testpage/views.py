from django.shortcuts import render

# Create your views here.

def index(request):
    username = request.session['username']
    return render(request, 'testpage/views.html' , {'username':username})