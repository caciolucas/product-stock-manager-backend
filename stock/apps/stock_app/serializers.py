from rest_framework import serializers

from .models import Category, Company, Product


class CategorySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Category

    def get_products(self, obj):
        products = Product.objects.filter(category=obj)
        return {
            "total_itens": products.count(),
            "itens": ProductSerializer(products, many=True).data,
            "total_quantity": sum(products.values_list("quantity", flat=True)),
        }


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.SerializerMethodField()

    class Meta:
        fields = "__all__"
        model = Company

    def get_products(self, obj):
        products = Product.objects.filter(supplier=obj)
        return {
            "total_itens": products.count(),
            "itens": ProductSerializer(products, many=True).data,
            "total_quantity": sum(products.values_list("quantity", flat=True)),
        }


class ProductSerializer(serializers.ModelSerializer):
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Company.objects.all(), source="supplier", write_only=True
    )

    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source="category", write_only=True
    )

    class Meta:
        fields = "__all__"
        model = Product
        depth = 1
