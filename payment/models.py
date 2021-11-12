from django.db import models


# Create your models here.
class carorder(models.Model):
    username = models.CharField(max_length=20)
    vehicle_id = models.IntegerField()
    weeks = models.IntegerField(default=1)
    price = models.IntegerField()
    payment_id = models.CharField(max_length=20)
    paid = models.BooleanField(default=False)
