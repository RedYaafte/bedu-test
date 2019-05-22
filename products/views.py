from django.shortcuts import render
from rest_framework import viewsets

from products.serializer import ProductSerializer
from products.models import Product


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
