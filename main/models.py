from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, related_name="books")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name="books")
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genre = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return self.title

