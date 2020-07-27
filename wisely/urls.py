from django.contrib import admin
from django.urls    import path,include

urlpatterns = [
    path('product',include('products.urls')),
]
