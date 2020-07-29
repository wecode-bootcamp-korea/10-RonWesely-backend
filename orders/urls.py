from django.urls    import path

from .views         import OrderColorItem,CartList

urlpatterns = [
    path('/color-select',OrderColorItem.as_view()),
    path('/cart-list',CartList.as_view()),
]
