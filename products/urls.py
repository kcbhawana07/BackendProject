from django.urls import path
from .views import *

urlpatterns = [
    path('get/', get_products),
    path('create/', create_product),
    path('update/', update_product),
    path('delete/', delete_product),
]