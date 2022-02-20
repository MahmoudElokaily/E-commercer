from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login

# Create your views here.


def signup(request):
    form = UserCreationForm()
    context = {
        'form' : form,
    }
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            print("Done1")
            user = form.save()
            print("Done2")
            auth_login(request , user)
            return redirect('http://127.0.0.1:8000/')
    return render(request , 'registration/signup.html' , context)