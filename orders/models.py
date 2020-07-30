from django.db import models

class Order(models.Model):
    user            = models.ForeignKey('users.User',on_delete=models.SET_NULL,null=True)
    shipping_price  = models.DecimalField(max_digits=10, decimal_places=2)
    list_price      = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price  = models.DecimalField(max_digits=10, decimal_places=2)
    total_price     = models.DecimalField(max_digits=10, decimal_places=2)
    order_status    = models.ForeignKey('OrderStatus',on_delete=models.SET_NULL,null=True)
    created_at      = models.DateTimeField(auto_now_add=True)
    ordered_at      = models.DateTimeField(null=True)
    shipping        = models.ForeignKey('users.Shipping',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'orders'

class OrderStatus(models.Model):
    name    = models.CharField(max_length=10)

    class Meta:
        db_table = 'order_statuses'

class OrderItem(models.Model):
    order           = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True)
    products_sizes  = models.ForeignKey('products.ProductSize',on_delete=models.SET_NULL,null=True)
    products_colors = models.ForeignKey('products.ProductColor',on_delete=models.SET_NULL,null=True)
    blade_products  = models.ForeignKey('products.BladeProduct',on_delete=models.SET_NULL,null=True)
    quantity        = models.IntegerField(default=0)
    discount_price  = models.DecimalField(max_digits=10, decimal_places=2)
    cart_at         = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'order_items'

class Review(models.Model):
    order_item  = models.ForeignKey('OrderItem',on_delete=models.SET_NULL,null=True)
    rate        = models.DecimalField(max_digits=10, decimal_places=2)
    review_text = models.CharField(max_length=200)
    writed_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'

class OrderImage(models.Model):
    image_url       = models.URLField(max_length=1000)
    products_sizes  = models.ForeignKey('products.ProductSize',on_delete=models.SET_NULL,null=True)
    products_colors = models.ForeignKey('products.ProductColor',on_delete=models.SET_NULL,null=True)
    blade_products  = models.ForeignKey('products.BladeProduct',on_delete=models.SET_NULL,null=True)

    class Meta:
        db_table = 'order_images'
