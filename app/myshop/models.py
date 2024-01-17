from typing import Any
from django.db import models
from django.urls import reverse


class Price(models.PositiveIntegerField):

    def __str__(self) -> str:
        value = self
        print(value)
        return super().__str__()


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(verbose_name="Show", default=True)
    is_new = models.BooleanField(verbose_name="Is new?", default=True)
    price = Price(verbose_name="Price")
    thumbnail = models.ImageField(
        upload_to='thumbnail/', default='thumbnail/default.png', verbose_name='Thumbnail')
    description = models.TextField(
        verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})


class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images",
                                null=False)
    image = models.ImageField()
