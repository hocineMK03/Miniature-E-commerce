# Generated by Django 4.1.7 on 2023-05-15 08:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_remove_categoryofcategories_categoryfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_categoryofcategories',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.categoryofcategories'),
            preserve_default=False,
        ),
    ]