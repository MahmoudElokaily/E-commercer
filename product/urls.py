from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name = 'home'),
    path('<str:name>' , views.category , name = 'category'),
    path('product_details/<int:id>/' , views.details , name='product_details'),
    path('add_new_product/' , views.add_new_product , name='add_new_product'),
    path('all_categories/', views.all_categories , name = 'all_categories'),
]