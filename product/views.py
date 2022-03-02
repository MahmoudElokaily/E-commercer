from django.shortcuts import render, redirect
from .models import *
from accounts.models import *
from .forms import *
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

def details(request,id):
    product = Product.objects.get(id=id)
    if request.method == 'POST':
        mycart = Cart.objects.get(user=request.user)
        mycart.product.add(product)
        return redirect('/')
    context = {
        'product' : product,
    }
    return render(request , 'product/product_details.html' , context)


def add_new_product(request):
    form = AddProductForm()
    if request.method == "POST":
        form = AddProductForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {
        'form' : form,
    }
    return render(request , 'product/addNewProduct.html' , context)


def all_categories(request):
    Categories = Category.objects.all()
    context = {
        'categories' : Categories,
    }
    return render(request , 'product/all_category.html' ,context)


