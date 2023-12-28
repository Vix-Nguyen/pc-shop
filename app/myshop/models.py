from djmoney.models.fields import MoneyField
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(verbose_name="Show", default=True)
    is_sold = models.BooleanField(verbose_name="Is sold?", default=True)
    price = MoneyField(max_digits=9, decimal_places=0, default_currency='VND')
    thumbnail = models.ImageField(upload_to='thumbnail/', default='thumbnail/default.png', verbose_name='Thumbnail')
    description = models.TextField(verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
