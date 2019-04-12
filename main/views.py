from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from user.models import User, Author
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            request.session['username'] = username
            return redirect('user/', username)
    else:

        form = UserCreationForm()
    return render(request, 'main/register.html', {'form' : form, 'valid': form.is_valid()})

