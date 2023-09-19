from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    active = models.BooleanField(name='active')
    price = models.PositiveIntegerField(name='Price')
