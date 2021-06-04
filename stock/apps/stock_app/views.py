import string as stringlib
from datetime import datetime

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import CategoryFilter, CompanyFilter, ProductFilter
from .models import Category, Company, Product
from .serializers import CategorySerializer, CompanySerializer, ProductSerializer


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

    # Could also you a filter
    @action(methods=["get"], detail=False, url_path="missing-stock")
    def missing_stock(self, request):
        companies = Company.objects.filter(product__quantity=0)
        return Response(CompanySerializer(companies, many=True).data)


class Task1View(APIView):
    def get(self, request):
        string = request.GET.get("string")
        if string:
            vowel = None
            start_time = datetime.now()

            alphabet = list(stringlib.ascii_lowercase)
            vowels = {"a", "e", "i", "o", "u"}
            consonants = list(set(alphabet) - set(vowels))

            can_be = []
            vowels_count = {vowel: 0 for vowel in vowels}
            for i in range(0, len(string)):
                if string[i].lower() in vowels:
                    vowels_count[string[i].lower()] += 1
                    if i > 2:
                        if (
                            string[i - 1].lower() in consonants
                            and string[i - 2].lower() in vowels
                        ):
                            can_be.append(string[i])

            repeated_vowels = [
                vowel for vowel, count in vowels_count.items() if count > 1
            ]

            for letter in can_be:
                if letter.lower() not in repeated_vowels:
                    vowel = letter

            end_time = datetime.now()
            execution_time = (end_time - start_time).total_seconds() * 1000

            return Response(
                {"string": string, "vogal": vowel, "tempoTotal": execution_time}
            )
        else:
            return Response(
                status=404, data={"message": "String not found", "ok": False}
            )
