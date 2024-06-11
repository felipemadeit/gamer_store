from django.db import models

# Create your models here.


class Product (models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default='non-category')
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)