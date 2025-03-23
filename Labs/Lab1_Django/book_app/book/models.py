from django.db import models
from django.db.models import ForeignKey
from django.contrib.auth.models import User


# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name} : {self.description}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    date_published = models.DateField()
    user_published = models.ForeignKey(User, on_delete=models.CASCADE)
    number_pages = models.IntegerField()
    book_cover = models.ImageField(upload_to="book_photos/", null=True, blank=True)
    available = models.BooleanField()

    def __str__(self):
        return f"{self.title} - {self.author}"


class Rating(models.Model):
    user = models.ForeignKey(User, models.CASCADE)
    grade = models.IntegerField()
    comment = models.CharField(max_length=100)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.grade}"


class Translator(models.Model):
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return f"{self.name} - {self.nationality}"


class BookTranslator(models.Model): # many-to-many
    translator = ForeignKey(Translator, on_delete=models.CASCADE)
    book = ForeignKey(Book, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book} {self.translator}"
