import random

from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(verbose_name="Show", default=False)
    is_new = models.BooleanField(verbose_name="Is new?", default=True)
    price = models.PositiveIntegerField(verbose_name="Price")
    thumbnail = models.ImageField(
        upload_to='thumbnail/', default='thumbnail/default.png', verbose_name='Thumbnail')
    description = models.TextField(
        verbose_name='Description', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})

    def get_related_products(self):
        all_products = Product.objects.exclude(id=self.id)

        if all_products.count() > 5:
            # Randomly select 4 products
            # TODO: Implement better strategy
            related_products = random.sample(list(all_products), 4)
        else:
            related_products = all_products

        return related_products


class ProductImage(models.Model):
    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name="images",
                                null=False)
    image = models.ImageField()
