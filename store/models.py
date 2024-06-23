from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    brand = models.CharField(max_length=200, default="Generic")
    description = models.TextField(default="None")
    primary_img = models.ImageField(upload_to='media/products', default=None)
    second_img = models.ImageField(upload_to='media/products',default=None)

    def get_format_price(self):
        return "${:,.0f}".format(self.price)
    
    def __str__(self):
        return self.name

