import datetime
from django.db import models
from cars.models import Car
from clients.models import Client


class Order(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateTimeField("Data zamówienia", default=datetime.datetime.now())
    from_date =  models.DateField("Data od", default=datetime.datetime.now().date())
    to_date =  models.DateField("Data do")

    def __str__(self):
        return "%s %s %s" % (self.car, self.client, self.order_date)

    class Meta:
        verbose_name = "Zamówienie"
        verbose_name_plural = "Zamówienie"
        ordering = ["client", "car", "order_date"]
