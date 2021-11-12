from django.db import models


# Create your models here.
class car(models.Model):
    name = models.CharField(max_length=25)
    category = models.CharField(max_length=10)
    price = models.IntegerField()
    image = models.ImageField()
