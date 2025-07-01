from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Distributor(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    year_founded = models.IntegerField()
    number_of_employees = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.year_founded}"


class Car(models.Model):

    TYPE_CAR = {
        "S" : "Sedan",
        "suv" : "SUV",
        "H" : "Hatchback",
        "C" : "Coupe",
    }

    distributor = models.ForeignKey(Distributor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number = models.IntegerField()
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    year_made = models.IntegerField()
    distance_km = models.IntegerField()
    type = models.CharField(choices=TYPE_CAR, max_length=15)
    image = models.ImageField(upload_to="car_images/", null=True, blank=True)

    def __str__(self):
        return f"{self.model} - {self.distributor} - {self.price}"
