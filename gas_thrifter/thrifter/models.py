from django.db import models


# Create your models here.
class GasPrices(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    station = models.CharField(max_length=50)

    

    def __str__(self):
        return f"Price is {self.price}$ at {self.station} station."

