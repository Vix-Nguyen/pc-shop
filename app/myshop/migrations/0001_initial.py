# Generated by Django 3.2.13 on 2023-12-29 18:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('active', models.BooleanField(default=True, verbose_name='Show')),
                ('is_sold', models.BooleanField(default=True, verbose_name='Is sold?')),
                ('price', models.PositiveIntegerField(verbose_name="Price")),
                ('thumbnail', models.ImageField(default='thumbnail/default.png', upload_to='thumbnail/', verbose_name='Thumbnail')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myshop.product')),
            ],
        ),
    ]
