from django.urls    import path

from .views         import (
    OrderColorItem,
    CartList,
    CheckOut,
    OrderBulkItem
)

urlpatterns = [
    path('/color-select',OrderColorItem.as_view()),
    path('/cart-list',CartList.as_view()),
    path('/checkout',CheckOut.as_view()),
    path('/bulk-order',OrderBulkItem.as_view()),
]
