from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    Categories = Category.objects.all()
    context = {
        'categories' : Categories,
    }
    return render(request , 'product/all_product.html' , context)


def category(request , name):
    category = Category.objects.get(name = name)
    context = {
        'category' : category,
    }
    return render(request , 'product/product.html' , context)