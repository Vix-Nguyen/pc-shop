from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage, Category

admin.site.register([Product, ProductImage, Category])
