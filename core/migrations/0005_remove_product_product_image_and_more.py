# Generated by Django 4.1.7 on 2023-05-14 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_product_product_image_product_product_stock_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='product_stock',
        ),
    ]
