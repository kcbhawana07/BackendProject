from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


# Create your views here.
#Create Order
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({"success": True})

    return Response({"success": False, "errors": serializer.errors})

#Get Orders
@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)

    return Response({
        "success": True,
        "data": serializer.data
    })
