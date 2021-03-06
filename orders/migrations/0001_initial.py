# Generated by Django 3.0.8 on 2020-07-27 01:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0007_delete_orderimage'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('ordered_at', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('discount_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('blade_products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.BladeProduct')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.Order')),
                ('products_colors', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductColor')),
                ('products_sizes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductSize')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'order_statuses',
            },
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('review_text', models.CharField(max_length=200)),
                ('writed_at', models.DateTimeField(auto_now_add=True)),
                ('order_item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.OrderItem')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='OrderImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=1000)),
                ('blade_products', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.BladeProduct')),
                ('products_sizes', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.ProductColor')),
            ],
            options={
                'db_table': 'order_images',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.OrderStatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='shipping',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.Shipping'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.User'),
        ),
    ]
