from email.policy import default
from importlib.metadata import requires
from django.db import models
class Cuisine(models.Model):
    cuisine = models.CharField(max_length=30)

class Restaurant(models.Model):
    Name = models.CharField(max_length=100)
    Location = models.CharField(max_length=100)
    Price = models.CharField(max_length=100)
    Cuisines = models.ManyToManyField(Cuisine)
    Rating = models.IntegerField()
    URL = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='', default='default.png')