from django.shortcuts import render
from .models import Booking, Hotel
from .forms import BookingForm

def booking_view(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            price = booking.total_price
            return render(request, 'booking_result.html', {'price': round(price, 2)})
    else:
        form = BookingForm()
    return render(request, 'booking.html', {'form': form})
