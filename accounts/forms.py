from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=255,required=True,widget=forms.EmailInput())
    image = forms.ImageField(allow_empty_file=True , required=False)
    country = forms.CharField(max_length=50)
    city = forms.CharField(max_length=50)
    phone_number = forms.CharField(max_length=11)
    class Meta:
        model = User
        fields = ['username' , 'email' , 'phone_number' , 'image' ,'password1' , 'password2' , 'country' , 'city']

