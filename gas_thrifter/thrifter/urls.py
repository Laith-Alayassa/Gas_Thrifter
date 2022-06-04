from django.urls import path
from . import views
from .views import GasPricesFormView


app_name = 'thrifter'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('form/', GasPricesFormView.as_view(), name = 'form'),
    path('thank_you', views.thank_you, name = 'thank_you')
]
