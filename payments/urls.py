from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/' , views.payment_page ,name="payment"),
    path('charge/<int:id>/' , views.charge , name ='charge'),
]