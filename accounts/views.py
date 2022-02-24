from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from .forms import *
from .models import *
from product.models import *

# Create your views here.


def signup(request):
    form = SignUpForm()
    context = {
        'form' : form,
    }
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request , user)
            return redirect('/')
    return render(request , 'registration/signup.html' , context)

def profile(request):
    profile = Profile.objects.get(user = request.user)
    context = {
        'profile' : profile,
    }
    print(profile.user.email)
    return render(request , 'accounts/profile.html' , context)


def profile_edit(request):
    profile = Profile.objects.get(user = request.user)
    userForm = UserForm(instance=request.user)
    profileForm = ProfileForm(instance=profile)
    if request.method == 'POST':
        userForm = UserForm(request.POST , instance=request.user)
        profileForm = ProfileForm(request.POST , request.FILES , instance=profile)
        if userForm.is_valid() and profileForm.is_valid():
            userForm.save()
            myprofile = profileForm.save(commit=False)
            myprofile.user = request.user
            myprofile.save()
            return redirect('/accounts/profile')

    context = {
        'userform': userForm,
        'profileform': profileForm,
    }
    return render(request , 'accounts/profile_edit.html' , context)


def my_cart(request):
    cart = Cart.objects.get(user=request.user)
    products = cart.product.all()
    context = {
        'cart' : cart,
        'products' : products
    }
    return render(request,'accounts/mycart.html' , context)