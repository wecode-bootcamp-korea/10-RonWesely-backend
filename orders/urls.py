from django.urls import path
from .views import ReviewView

urlpatterns = [
    path('/Review', ReviewView.as_view())
]
