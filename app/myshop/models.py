import random

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    order = models.IntegerField("order", default=20)
    slug = models.SlugField(unique=True, null=True)
    parent_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    @classmethod
    def get_category_by_level(cls):
        categs = cls.objects.filter(parent_category=None).order_by("order").all()
        res = [
            {
                "name": categ.name,
                "slug": categ.slug,
                "subcategs":categ.subcategories.order_by("order").all()
            }
            for categ in categs
        ]
        return res

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    active = models.BooleanField(verbose_name="Show", default=True)
    price = models.PositiveIntegerField(verbose_name="Price")
    category = models.ForeignKey(
        Category, verbose_name="Category", null=True, on_delete=models.SET_NULL)
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
