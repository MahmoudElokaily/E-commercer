from .serializers import *
from rest_framework import generics
from .models import *

class ProductListAPI(generics.ListAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class ProductDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    model = Product
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'id'

class CategoriesListAPI(generics.ListAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializers


class CategoryDetailsAPI(generics.RetrieveUpdateDestroyAPIView):
    model = Category
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializers
    lookup_field = 'id'