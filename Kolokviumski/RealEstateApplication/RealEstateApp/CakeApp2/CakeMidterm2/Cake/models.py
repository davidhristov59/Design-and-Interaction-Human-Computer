from django.contrib.auth.models import User
from django.db import models
from django.db.models import ForeignKey


# Create your models here.
class Cake(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()
    weight = models.IntegerField()
    description = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    baker = models.ForeignKey('Baker', on_delete=models.CASCADE, related_name='cakes') # (many cakes can belong to one baker).

    def __str__(self):
        return f"{self.name} - {self.price}"

class Baker(models.Model):
    name = models.CharField(max_length=20)
    surname = models.CharField(max_length=20)
    phone = models.IntegerField()
    email = models.EmailField()
    user = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} {self.surname}"
