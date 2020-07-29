# Generated by Django 3.0.8 on 2020-07-29 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20200728_1940'),
    ]

    operations = [
        migrations.CreateModel(
            name='RazorColor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=1000)),
                ('color', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='products.Color')),
            ],
            options={
                'db_table': 'razor_colors',
            },
        ),
    ]
