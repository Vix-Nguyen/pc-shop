from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(verbose_name="Active")
    price = models.PositiveIntegerField(default=0, verbose_name='Price')
    thumbnail = models.ImageField(upload_to='thumbnail/', default='thumbnail/default.png', verbose_name='Thumbnail')

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField()
