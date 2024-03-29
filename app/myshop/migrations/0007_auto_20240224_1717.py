# Generated by Django 3.2.13 on 2024-02-24 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myshop', '0006_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_new',
        ),
        migrations.AddField(
            model_name='category',
            name='order',
            field=models.IntegerField(default=20, verbose_name='order'),
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Show'),
        ),
    ]
