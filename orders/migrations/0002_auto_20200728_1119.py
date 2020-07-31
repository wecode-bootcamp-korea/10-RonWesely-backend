# Generated by Django 3.0.8 on 2020-07-28 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_delete_orderimage'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderimage',
            name='products_colors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductColor'),
        ),
        migrations.AlterField(
            model_name='orderimage',
            name='products_sizes',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductSize'),
        ),
    ]
