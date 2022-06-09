from django.contrib import admin

from .models import Cities, GasPrices,Station

# Register your models here.
admin.site.register(GasPrices)
admin.site.register(Cities)
admin.site.register(Station)
