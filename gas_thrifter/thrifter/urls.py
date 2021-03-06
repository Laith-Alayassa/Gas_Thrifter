from django.urls import path
from . import views
from .views import GasPricesCreateView, register

app_name = 'thrifter'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', GasPricesCreateView.as_view(), name = 'create'),
    path('list/', views.list_view, name = 'list_view'),
    path('thank_you', views.thank_you, name = 'thank_you'),
    path('map/<str:station>', views.station_map, name = 'station_map'),
    path('register/', views.register , name = 'register')
]


# TODO: create a random price generator that runs everyday and generates numbers and prices
# TODO: create a graph over time of where are these prices
# TODO: add google maps to all of this