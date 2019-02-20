from django.db import models
import datetime


# Create your models here.
class Car(models.Model):
    CAR_TYPES = (
        ("A", "Klasa A"),
        ("B", "Klasa B"),
        ("DUPA", "Klasa DUPA")
    )
    brand = models.CharField("Marka", max_length=50)
    name = models.CharField("Model", max_length=50)
    type = models.CharField("Typ", max_length=10, choices=CAR_TYPES, default=CAR_TYPES[0])
    manufacture_year = models.IntegerField("Rok produkcji", default=datetime.datetime.now().year)
    capacity = models.FloatField("Pojemność")
    price = models.FloatField("Cena", null=True)

    def __str__(self):
        return "%s %s" % (self.brand, self.name)

    class Meta:
        verbose_name = "Samochód "
        verbose_name_plural = "Samochody"
        ordering = ["brand", "name"]
