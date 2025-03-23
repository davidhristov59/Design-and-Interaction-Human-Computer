from django.db import models
from django.contrib.auth.models import User


class Balloon(models.Model):
    TYPE_CHOICES = {
        "S" : "Small Balloon",
        "M" : "Medium Balloon",
        "L" : "Large Balloon"
    }

    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    max_passengers = models.IntegerField()

    def __str__(self):
        return f"{self.name} - manufacturer {self.manufacturer}"


class Pilot(models.Model):

    RANK_CHOICES = {
        "J" : "Junior",
        "I" : "Intermediate",
        "S" : "Senior"
    }

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    date_birth = models.DateField()
    total_hours_on_flight = models.DecimalField(max_digits=5, decimal_places=2)
    rank = models.CharField(max_length=1, choices=RANK_CHOICES)

    def __str__(self):
        return f"{self.name} {self.surname} - rank {self.rank}"


class Airline(models.Model):
    name = models.CharField(max_length=100)
    year_founded = models.IntegerField()
    europe = models.BooleanField()

    def __str__(self):
        return f"{self.name} - {self.year_founded} "


class AirlinePilot(models.Model):
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pilot} - {self.airline}"


# Create your models here.
class Flight(models.Model):
    code = models.CharField(max_length=100, unique=True)
    take_off_airport = models.CharField(max_length=100)
    landing_airport = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="flight_photos/", null=True, blank=True)
    balloon = models.ForeignKey(Balloon, on_delete=models.CASCADE)
    pilot = models.ForeignKey(Pilot, on_delete=models.CASCADE)
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.code} {self.take_off_airport} - {self.landing_airport}"
