from django.urls import path
from .views import register,logout,RegisterView,LogoutView

urlpatterns = [
    path('register/', register),
    path('logout/', logout),
    path('registerclass/', RegisterView.as_view()),
    path('logoutclass/', LogoutView.as_view()),
]

