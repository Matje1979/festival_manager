from django.db import models
from location_field.models.plain import PlainLocationField
from django_google_maps import fields as map_fields
# Create your models here.

class Event(models.Model):
    name=models.CharField(max_length=50, verbose_name="Ime")
    beggining=models.DateTimeField(verbose_name="Početak")
    end=models.DateTimeField(verbose_name="Kraj")
    country=models.CharField(max_length=30)
    city=models.CharField(max_length=30, verbose_name="Grad")
    address=models.CharField(max_length=50,verbose_name="Adresa")
    location = PlainLocationField(based_fields=['city'], default = '44.7857606, 20.4776834', zoom=8, verbose_name="Lokacija")
    description = models.TextField(default="Detalji slede uskoro...", verbose_name="Opis")
    # geolocation = map_fields.GeoLocationField(max_length=100)
    image=models.ImageField(default="default.jpg", upload_to='images', verbose_name="Slika")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Vreme kreiranja dogadjaja")
    last_updated=models.DateTimeField(auto_now=True, verbose_name="Vreme poslednje izmene")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Dogadjaji"
        verbose_name = "Dogadjaj"

    def get_absolute_url(self):
        return reverse('app-home')


class Visitor(models.Model):
    first_name=models.CharField(max_length=50, verbose_name="Ime")
    last_name=models.CharField(max_length=50, verbose_name="Prezime")
    email=models.EmailField(verbose_name="Emejl")
    event=models.ForeignKey(Event, on_delete=models.CASCADE, verbose_name="Dogadjaj")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name_plural = "Posetioci"
        verbose_name = "Posetioc"



