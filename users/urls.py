from django.urls import path
from .views import register,logout

urlpatterns = [
    path('register/', register),
    path('logout/', logout),
]

