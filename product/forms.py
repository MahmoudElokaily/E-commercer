from django import forms
from .models import *

class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name' , 'image' , 'price' , 'type' , 'category']