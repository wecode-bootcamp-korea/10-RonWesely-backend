from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table = 'categories'

class Product(models.Model):
    category        = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    name            = models.CharField(max_length=20)
    description     = models.CharField(max_length=50)
    product_size    = models.ManyToManyField('Size',through='ProductSize')
    product_color   = models.ManyToManyField('Color',through='ProductColor')

    class Meta:
        db_table = 'products'

class BladeProduct(models.Model):
    product     = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'blade_products'

class Size(models.Model):
    name        = models.CharField(max_length=20)
    description = models.CharField(max_length=10,null=True)

    class Meta:
        db_table = 'sizes'

class Color(models.Model):
    name    = models.CharField(max_length=20)

    class Meta:
        db_table = 'colors'

class SkinType(models.Model):
    name    = models.CharField(max_length=10)

    class Meta:
        db_table = 'skin_types'

class ProductColor(models.Model):
    product = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    color   = models.ForeignKey('Color',on_delete=models.SET_NULL,null=True)
    price   = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        db_table = 'products_colors'

class ProductSize(models.Model):
    product     = models.ForeignKey('Product',on_delete=models.SET_NULL,null=True)
    size        = models.ForeignKey('Size',on_delete=models.SET_NULL,null=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    skin_type   = models.ForeignKey('SkinType',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'products_sizes'

class RazorColor(models.Model):
    color       = models.ForeignKey('Color',on_delete=models.SET_NULL,null=True)
    eng_name    = models.CharField(max_length=20,null=True)
    image_url   = models.URLField(max_length=1000)

    class Meta:
        db_table = 'razor_colors'

