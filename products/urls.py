from django.urls    import path

from .views         import ProductDetail

urlpatterns = [
    path('/<int:product_id>',ProductDetail.as_view()),
]
