# Generated by Django 3.0.8 on 2020-07-24 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_remove_productsize_description'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderImage',
        ),
    ]