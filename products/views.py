from django.shortcuts import render
from rest_framework.decorators import api_view#converts function into API
from rest_framework.response import Response#sends JSON response
from .models import Product#your database model
from .serializers import ProductSerializer#converts model ↔ JSON

# Create your views here.

#Get all product 
@api_view(['GET'])
def get_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)

    return Response({
        "success": True,
        "data": serializer.data
    })


#Create product 
@api_view(['POST'])
def create_product(request):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})

    return Response({"success": False, "errors": serializer.errors})


#Update product
@api_view(['PUT'])
def update_product(request, id):
    product = Product.objects.get(id=id)
    serializer = ProductSerializer(product, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})

    return Response({"success": False})



#Delete product 
@api_view(['DELETE'])
def delete_product(request, id):
    product = Product.objects.get(id=id)
    product.delete()

    return Response({"success": True})