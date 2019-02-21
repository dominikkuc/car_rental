from django.db import models


# Create your models here.
class Client(models.Model):
    first_name = models.CharField("Imię", max_length=50)
    last_name = models.CharField("Nazwisko", max_length=50)
    email = models.CharField("Email", max_length=50)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klienci"
        ordering = ["first_name", "last_name", "email"]
