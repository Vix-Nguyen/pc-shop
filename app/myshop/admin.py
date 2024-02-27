from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Category, Thumbnail

admin.site.register([Product, ProductImage, Category, Thumbnail])
