# hotel_app/views.py

from django.shortcuts import render
from django.http import HttpResponse
from math import pow
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

def calculate_dynamic_price(base_price, length_of_stay, booking_advance, num_persons, flexible_cancellation):
    length_of_stay_factor = 1.1
    booking_advance_factor = 0.95
    num_persons_factor = 1.2
    cancellation_factor = 0.9 if flexible_cancellation else 1.0

    dynamic_price = base_price * pow(length_of_stay_factor, length_of_stay) * pow(booking_advance_factor, booking_advance) * pow(num_persons_factor, num_persons) * cancellation_factor
    return dynamic_price
def hotel(request):
    return render(request, 'hotel_pricing.html')
def hotel_pricing(request):

    if request.method == "POST":
        # Assuming these values are passed from a form in the frontend
        base_price = float(request.POST.get('base_price'))
        length_of_stay = int(request.POST.get('length_of_stay'))
        booking_advance = int(request.POST.get('booking_advance'))
        num_persons = float(request.POST.get('num_persons'))
        flexible_cancellation = request.POST.get('flexible_cancellation') == 'true'

        price = calculate_dynamic_price(base_price, length_of_stay, booking_advance, num_persons, flexible_cancellation)
        return HttpResponse(f"Calculated Price: ${price:.2f}")


    return render(request, 'hotel_pricing.html')
def calculate_dates(request):
    if request.method == 'POST':
        form = DateFilterForm(request.POST)
        if form.is_valid():
            from_date = form.cleaned_data['from_date']
            to_date = form.cleaned_data['to_date']

            date_list = []
            current_date = from_date
            while current_date <= to_date:
                is_weekend = current_date.weekday() in [5, 6]  # 5=Saturday, 6=Sunday
                date_entry, created = DateEntry.objects.get_or_create(
                    date=current_date, defaults={'is_weekend': is_weekend}
                )
                date_list.append(date_entry)
                current_date += timedelta(days=1)

            return render(request, 'date_calculator/result.html', {'date_list': date_list})

    else:
        form = DateFilterForm()