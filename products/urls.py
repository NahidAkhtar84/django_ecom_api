from django.urls import path
from .views import All_Products, Product_Det

urlpatterns = [
    path('api/all_products', All_Products.as_view(), name='all_products_api'),
    path('api/all_products/<int:pk>/', Product_Det.as_view(), name='detail_product_api'),
]