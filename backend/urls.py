"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT Auth creates a login endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT Auth creates a token refresh endpoint
#
    path('users/', include('users.urls')),#Users
    
    path('products/', include('products.urls')),#Products

    path('orders/', include('orders.urls')),#Orders
]

##Simple Summary (Exam Ready)
#api/token/ → login API (get tokens)
#api/token/refresh/ → get new access token
#.as_view() → converts class view to function
#Access token → used to access APIs
#Refresh token → used to renew access token