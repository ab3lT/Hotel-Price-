from django.shortcuts import render
from .forms import DateInputForm
from .models import HotelPrice
import datetime
from decimal import Decimal
from django.shortcuts import render
from django.shortcuts import redirect

def choose_option(request):
    return render(request, 'choose_option.html')

def ajax_view(request):
    if request.is_ajax() and request.method == 'POST':
        user_selection = request.POST.get('selection')
        # Logic to determine the redirect URL based on the selection
        redirect_url = '/some-url/'  # Example URL
        return JsonResponse({'redirect_url': redirect_url})
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
    
def handle_option(request):
    if request.method == 'POST':
        choice = request.POST.get('option')
        if choice == 'option1':
            return redirect('option1')
        elif choice == 'option2':
            return redirect('option2')
    
    # If no choice is made or an invalid choice is submitted, return to the choose_option page.
    return redirect('choose_option')



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


def option1(request):
    return render(request, 'option1.html')

def option2(request):
    return render(request, 'option2.html')