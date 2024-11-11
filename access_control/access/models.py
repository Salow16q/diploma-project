from django.db import models

class AllowedVehicle(models.Model):
    license_plate = models.CharField(max_length=20, unique=True)
    description = models.TextField(blank=True)

class Event(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    license_plate = models.CharField(max_length=20)
    allowed = models.BooleanField()
    image = models.ImageField(upload_to='events/')