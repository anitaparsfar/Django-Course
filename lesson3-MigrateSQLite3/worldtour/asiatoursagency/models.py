from django.db import models

# Create your models here.
class Tour(models.Model):
    # we need a origin country, we need a destination, number of nights, price for the tour
    origin_country = models.CharField(max_length=64)
    num_of_nights = models.IntegerField()
    destination_country = models.CharField(max_length=64)
    price = models.IntegerField()