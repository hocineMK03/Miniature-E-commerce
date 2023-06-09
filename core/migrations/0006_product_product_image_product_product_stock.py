# Generated by Django 4.1.7 on 2023-05-14 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_product_product_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default=1, upload_to='static/images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_stock',
            field=models.IntegerField(default=0),
        ),
    ]
