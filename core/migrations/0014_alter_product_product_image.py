# Generated by Django 4.1.7 on 2023-05-21 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
