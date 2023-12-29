
from django.urls import path
from .views import hotel_pricing, hotel

urlpatterns = [
        path('', hotel_pricing, name='hotel_pricing'),
]