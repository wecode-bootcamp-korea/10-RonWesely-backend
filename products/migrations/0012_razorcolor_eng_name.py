# Generated by Django 3.0.8 on 2020-07-30 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_razorcolor'),
    ]

    operations = [
        migrations.AddField(
            model_name='razorcolor',
            name='eng_name',
            field=models.CharField(max_length=10, null=True),
        ),
    ]