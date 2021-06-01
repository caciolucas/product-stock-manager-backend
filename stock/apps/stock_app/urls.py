from django.urls import include, path
from rest_framework import routers

from stock.apps.stock_app import views

router = routers.DefaultRouter()
router.register("product", views.ProductViewSet)
router.register("company", views.CompanyViewSet)
router.register("category", views.CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
