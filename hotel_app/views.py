from django.shortcuts import render
from .forms import DateInputForm
from .models import HotelPrice
import datetime
from decimal import Decimal


def calculate_price(request):
    form = DateInputForm(request.POST or None)
    total_price = 0

    if form.is_valid():
        check_in = form.cleaned_data['check_in']
        check_out = form.cleaned_data['check_out']
        booking_advance = form.cleaned_data['booking_advance']
        num_persons = form.cleaned_data['num_persons']
        flexible_cancellation = form.cleaned_data['flexible_cancellation']

        price_obj = HotelPrice.objects.first()  # Assuming you have at least one price object

        for single_date in (check_in + datetime.timedelta(n) for n in range((check_out - check_in).days)):
            daily_rate = price_obj.weekday_rate if single_date.weekday() < 5 else price_obj.weekend_rate
            total_price += daily_rate * num_persons

        # Apply discounts or extra fees
        if booking_advance and booking_advance > 14:  # For example, 10% discount for advance bookings
            discount_factor = Decimal('0.9')  
            total_price *= discount_factor

        if flexible_cancellation:
            cancellation_fee_factor = Decimal('1.05')  
            total_price *= cancellation_fee_factor

    return render(request, 'price_calculator.html', {'form': form, 'total_price': total_price})