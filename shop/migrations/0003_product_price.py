# Generated by Django 4.1.5 on 2023-02-15 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_category_product_image_product_subcategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
