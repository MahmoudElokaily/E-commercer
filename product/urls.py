from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'home'),
    path('<str:name>' , views.category , name = 'category'),
]