# Generated by Django 3.2.13 on 2024-01-17 04:18

from django.db import migrations
import myshop.models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0002_auto_20240117_0313'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='price_currency',
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=myshop.models.Price(verbose_name='Price'),
        ),
    ]
