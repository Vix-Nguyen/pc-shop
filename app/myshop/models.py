from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(name='active')
    price = models.PositiveIntegerField(default=0)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
