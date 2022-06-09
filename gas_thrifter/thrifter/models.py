from pickle import TRUE
from django.db import models


# Create your models here.


class Cities(models.Model):
    city = models.CharField(max_length=50, unique=TRUE)

    def __str__(self):
        return f"City is {self.city}"


class Station(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GasPrices(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    station = models.ForeignKey(Station, on_delete=models.CASCADE, default="NA")
    city = models.ForeignKey(Cities, on_delete=models.CASCADE, default="NA")
    address = models.CharField(max_length=100, default="NA")

    def __str__(self):
        return f"Price is {self.price}$ at {self.station} station in {self.city} at time {self.time.strftime('%d/%b/%y %-H:%M')}"
