# Generated by Django 4.1.7 on 2023-05-14 13:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_categoryofcategories_categoryfrom'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryofcategories',
            name='categoryfrom',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.category'),
            preserve_default=False,
        ),
    ]
