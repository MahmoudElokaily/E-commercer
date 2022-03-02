import stripe
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
from product.models import *

# Create your views here.


def payment_page(request,id):
    product = Product.objects.get(id=id)
    context = {
        'key' : settings.STRIPE_PUBLISHABLE_KEY,
        'product' : product
    }
    return render(request , 'payments/payment.html' , context)


def charge(request,id):
    if request.method == "POST":
        charge = stripe.Charge.create(
            amount = 1,
            currency = "usd",
            description = "Payment Gateway",
            source = request.POST['stripeToken'],
            api_key = settings.STRIPE_SECRET_KEY

        )
        delete_product(id)
        return render(request , 'payments/charge.html')



def delete_product(id):
    product = get_object_or_404(Product , id=id)
    product.delete()