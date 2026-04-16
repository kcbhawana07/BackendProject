# from django.db import models
# from django.contrib.auth.models import AbstractUser
# # Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
    

# class User(AbstractUser):
#     email = models.EmailField(unique=True)

#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['email']
from django.contrib.auth.models import AbstractUser #Add extra fields (phone, address, etc.)
from django.db import models
class User(AbstractUser):
    email = models.EmailField(unique=True)

