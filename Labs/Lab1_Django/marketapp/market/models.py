from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Product(models.Model):

    TYPE_CHOICES = {
        "F" : "Food",
        "D" : "Drinks",
        "B" : "Bakery",
        "C" : "Cosmetics",
        "H" : "Hygiene"
    }

    name = models.CharField(max_length=100)
    type_product = models.CharField(max_length=1, choices=TYPE_CHOICES)
    product_home_country = models.BooleanField()
    code = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.name} - {self.code}"


class Market(models.Model):
    name = models.CharField(max_length=100)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    # contact_info = models.CharField(max_length=100)
    num_markets = models.IntegerField()
    date_opened = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    closing_time_from = models.TimeField()
    closing_time_to = models.TimeField()

    def __str__(self):
        return f"{self.name} - {self.closing_time_from} : {self.closing_time_to}"


class ProductInMarket(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.market.name} {self.product.name} {self.quantity}"


class ContactInfo(models.Model):
    street = models.CharField(max_length=100)
    street_number = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email_address = models.EmailField()
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.street} {self.street_number} - {self.phone_number} {self.email_address}"


class Employee(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=13)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    salary = models.DecimalField(decimal_places=2, max_digits=4)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname} {self.ssn}"
        


