# Generated by Django 3.0.8 on 2020-07-24 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20200724_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='productsize',
            name='description',
            field=models.CharField(max_length=10, null=True),
        ),
    ]