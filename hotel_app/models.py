from django.db import models

class HotelPrice(models.Model):
    weekday_rate = models.DecimalField(max_digits=6, decimal_places=2)
    weekend_rate = models.DecimalField(max_digits=6, decimal_places=2)