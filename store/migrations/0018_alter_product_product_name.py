# Generated by Django 5.0.6 on 2024-06-19 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_rename_categorie_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=300),
        ),
    ]
