from django_filters import rest_framework as filters

from .models import Category, Company, Product


class ProductFilter(filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            "name": ["contains"],
            "quantity": ["exact", "gte", "gt", "lte", "lt"],
        }


class CategoryFilter(filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            "name": ["iexact", "contains", "icontains"],
        }


class CompanyFilter(filters.FilterSet):
    class Meta:
        model = Company
        fields = {
            "name": ["iexact", "contains", "icontains"],
        }
