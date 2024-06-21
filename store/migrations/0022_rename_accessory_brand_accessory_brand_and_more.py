# Generated by Django 5.0.6 on 2024-06-21 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_mouse_mouse_img'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='accessory',
            old_name='accessory_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='case',
            old_name='case_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='chair',
            old_name='chair_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='graphics_card',
            old_name='card_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='headphones',
            old_name='headPhones_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='keyboard',
            old_name='keyboard_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='laptop',
            old_name='laptop_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='monitor',
            old_name='monitor_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='motherboard',
            old_name='motherBoard_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='mouse',
            old_name='mouse_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='power_supply',
            old_name='power_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='processor',
            old_name='processor_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='ram',
            old_name='ram_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='refrigeration',
            old_name='refrigeration_stock',
            new_name='stock',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_brand',
            new_name='brand',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_date_created',
            new_name='date_created',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_date_modified',
            new_name='date_modified',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_img',
            new_name='img',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_price',
            new_name='price',
        ),
        migrations.RenameField(
            model_name='storage',
            old_name='storage_stock',
            new_name='stock',
        ),
    ]