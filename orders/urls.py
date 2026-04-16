from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_orders), # Get orders
    path('create/', create_order),# POST create order
]