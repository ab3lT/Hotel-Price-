from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    weekday_price = models.FloatField()
    weekend_price = models.FloatField()
    def __str__(self):
        return(f"{self.name}")

class Booking(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    num_persons = models.IntegerField()
    flexible_cancellation = models.BooleanField()
    def __str__(self):
        return(f"{self.hotel.name}  From {self.start_date} To {self.end_date} number of persons: {self.num_persons}  Flexible cancellation: {self.flexible_cancellation}")

    @property
    def total_price(self):
        # Calculate total price based on factors
        length_of_stay = (self.end_date - self.start_date).days
        length_of_stay_factor = 1.1
        booking_advance_factor = 0.95
        num_persons_factor = 1.2
        cancellation_factor = 0.9 if self.flexible_cancellation else 1.0

        base_price = self.hotel.weekday_price  # or weekend price based on date

        price = base_price * length_of_stay * length_of_stay_factor * \
                booking_advance_factor * num_persons_factor * cancellation_factor
        return price
    
 