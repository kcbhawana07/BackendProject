from django.db import models

# Create your models here.

class Order(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"Order {self.id}"