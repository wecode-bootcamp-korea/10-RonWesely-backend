from django.db import models

class Category(models.Model):
    name        =   models.CharField(max_length=20)
    description =   models.CharField(max_length=50)

    class Meta:
        db_table = 'categories'

class BladeProduct(models.Model):
    category    =   models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    name        =   models.CharField(max_length=20)
    description =   models.CharField(max_length=20,null=True)
    price       =   models.IntegerField()

    class Meta:
        db_table = 'blade_products'

class RazorProduct(models.Model):
    category    =   models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    name        =   models.CharField(max_length=20)
    description =   models.CharField(max_length=20,null=True)

    class Meta:
        db_table = 'razor_products'

class SkinProduct(models.Model):
    category    =   models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    name        =   models.CharField(max_length=20)
    description =   models.CharField(max_length=20,null=True)

    class Meta:
        db_table = 'skin_products'

class Size(models.Model):
    name    =   models.CharField(max_length=20)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    name    =   models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'

class RazorProductColor(models.Model):
    razor_product   =   models.ForeignKey('RazorProduct',on_delete=models.SET_NULL,null=True)
    name            =   models.CharField(max_length=20)
    color           =   models.ForeignKey('Color',on_delete=models.SET_NULL,null=True)
    price           =   models.IntegerField()

    class Meta:
        db_table = 'razor_products_colors'

class SkinProductSize(models.Model):
    skin_product    =   models.ForeignKey('SkinProduct',on_delete=models.SET_NULL,null=True)
    name            =   models.CharField(max_length=20)
    size            =   models.ForeignKey('Size',on_delete=models.SET_NULL,null=True)
    price           =   models.IntegerField()

    class Meta:
        db_table = 'skin_products_sizes'

class OrderImage(models.Model):
    image_url               =   models.URLField(max_length=1000)
    razor_products_colors   =   models.ForeignKey('RazorProductColor',on_delete=models.SET_NULL,null=True)
    skin_products_sizes     =   models.ForeignKey('SkinProductSize',on_delete=models.SET_NULL,null=True)
    blade_products          =   models.ForeignKey('BladeProduct',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'order_images'
