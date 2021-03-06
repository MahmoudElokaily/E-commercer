from django.urls import path
from . import views,api

urlpatterns = [
    path('' , views.index , name = 'home'),
    path('<str:name>' , views.category , name = 'category'),
    path('product_details/<int:id>/' , views.details , name='product_details'),
    path('add_new_product/' , views.add_new_product , name='add_new_product'),
    path('all_categories/', views.all_categories , name = 'all_categories'),
    # API
    path('api/products/' , api.ProductListAPI.as_view() , name = 'product_list_api'),
    path('api/product/<int:id>/' , api.ProductDetailsAPI.as_view() , name = 'product_detail_api'),
    path('api/categories/' , api.CategoriesListAPI.as_view() , name = 'category_list_api'),
    path('api/category/<int:id>/', api.CategoryDetailsAPI.as_view(), name='category_detail_api'),

]