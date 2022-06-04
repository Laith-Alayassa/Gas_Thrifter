from dataclasses import fields
from django.forms import ModelForm
from .models import GasPrices


class GasPricesForm(ModelForm):
    class Meta:
        model = GasPrices
        fields = "__all__"
        exclude = ("",)
