from django.shortcuts import render
# Create your views here.
from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.decorators import action

from .filters import CategoryFilter, CompanyFilter, ProductFilter
from .models import Category, Company, Product
from .serializers import (CategorySerializer, CompanySerializer,
                          ProductSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_class = ProductFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_class = CategoryFilter


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filter_class = CompanyFilter
