from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_products), # GET all products (CRUD OPEARATION)
    path('create/', create_product),# POST create product
    path('update/', update_product),# PUT update product
    path('delete/', delete_product),# DELETE product
]