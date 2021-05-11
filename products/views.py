from django.shortcuts import render
from rest_framework.views import APIView, Response
from rest_framework import generics

# Product
from .serializers import ProductSerializers, ProductDetailSerializer
from .models import Product
from rest_framework import status

# Create your views here.

class All_Products(generics.ListCreateAPIView):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()

# class Product_Details(id, generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = ProductSerializers
#     queryset = Product.objects.filter(id=id)

class Product_Det(APIView):
    def get(self, request, pk):
        try:
            detail_product = Product.objects.get(id=pk)
            serializer = ProductDetailSerializer(detail_product)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            detail_product = Product.objects.get(id=pk)
            serializer = ProductDetailSerializer(detail_product, data=request.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            detail_product = Product.objects.get(id=pk)
            detail_product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)





