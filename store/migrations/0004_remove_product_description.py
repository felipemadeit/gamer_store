# Generated by Django 5.0.6 on 2024-06-10 23:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_product_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
    ]