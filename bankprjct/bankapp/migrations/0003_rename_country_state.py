# Generated by Django 4.1 on 2023-01-15 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankapp', '0002_rename_categor_material_remove_product_category_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Country',
            new_name='State',
        ),
    ]
