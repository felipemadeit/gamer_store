# Generated by Django 5.0.6 on 2024-06-12 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_products_product_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='product_brand',
            field=models.CharField(default='general', max_length=200),
        ),
    ]
