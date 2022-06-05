from django.urls import path
from . import views
from .views import GasPricesCreateView, GasPricesFormListView


app_name = 'thrifter'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', GasPricesCreateView.as_view(), name = 'create'),
    path('list/', GasPricesFormListView.as_view(), name = 'list_View'),
    path('thank_you', views.thank_you, name = 'thank_you')
]
