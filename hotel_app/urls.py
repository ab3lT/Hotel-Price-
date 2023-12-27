from django.urls import path
from .views import hotel_pricing

urlpatterns = [
    path('hotel-pricing/', hotel_pricing, name='hotel_pricing'),
]