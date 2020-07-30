from django.urls    import path

from .views         import (
    ProductDetail,
    ColorDetail
)

urlpatterns = [
    path('/<int:product_id>',ProductDetail.as_view()),
    path('/color-detail',ColorDetail.as_view()),
]
