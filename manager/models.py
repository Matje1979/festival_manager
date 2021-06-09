from django.db import models
from location_field.models.plain import PlainLocationField
from django_google_maps import fields as map_fields
# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=50)
    beggining=models.DateTimeField()
    end=models.DateTimeField()
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    address=models.CharField(max_length=50)
    location = PlainLocationField(based_fields=['city'], default = '44.7857606, 20.4776834', zoom=8)
    # geolocation = map_fields.GeoLocationField(max_length=100)
    image=models.ImageField(default="default.jpg", upload_to='images')
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Visitor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.EmailField()
    event=models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'



