# Generated by Django 3.0.8 on 2020-07-23 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bladeproduct',
            old_name='category',
            new_name='product',
        ),
    ]