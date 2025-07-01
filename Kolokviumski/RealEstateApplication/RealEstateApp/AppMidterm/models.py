from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Property(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateField(auto_now_add=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name}"

class Agent(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    linkedin = models.CharField(max_length=50)
    number_sold_properties = models.IntegerField()
    email = models.EmailField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"

class AgentProperties(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)

class Characteristics(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField()


class CharacteristicsProperties(models.Model):
    characteristics = models.ForeignKey(Characteristics, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
