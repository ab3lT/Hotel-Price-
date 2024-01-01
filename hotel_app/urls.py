
# from django import views
# from django.urls import path
# from .views import calculate_price, choose_option, handle_option,  option1, option2, ajax_view

# urlpatterns = [
#         path('', choose_option, name='hotel_pricing'),
#         # path('handle_option/', views.handle_option.aste),
#     # path('option1/', views.option1, name='option1'),  # Add option1 and option2 views if needed
#     # path('option2/', views.option2, name='option2'),  # Add optio
#         path('/choice', calculate_price, name='hotel_pricing'),
#           path('ajax-view-url/', views.ajax_view.as_view(), name='ajax_view'),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.booking_view, name='booking_view'),
 
]