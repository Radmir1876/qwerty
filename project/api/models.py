from django.db import models

class Product (models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ManyToManyField('Category')
    size = models.CharField(max_length=100)
    Manufacturer = models.CharField(max_length=100)


    def __str__(self):
        return self.title

class Category (models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

class Manufacturer (models.Model):
    name = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
# Create your models here.
