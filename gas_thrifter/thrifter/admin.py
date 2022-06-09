from django.contrib import admin

from .models import Cities, GasPrices

# Register your models here.
admin.site.register(GasPrices)
admin.site.register(Cities)
