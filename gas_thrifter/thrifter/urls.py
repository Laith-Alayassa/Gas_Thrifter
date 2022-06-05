from django.urls import path
from . import views
from .views import GasPricesCreateView # , GasPricesFormListView


app_name = 'thrifter'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('create/', GasPricesCreateView.as_view(), name = 'create'),
    # path('list/', GasPricesFormListView.as_view(), name = 'list_View'), //will try and use a method instead of class to do easy filtering
    # path('list/', views.list_view, name = 'list_view'),
    path('list/', views.list_view, name = 'list_view'),
    # path('list/<str:max_price>', views.list_view_filtered, name = 'list_view'),
    path('thank_you', views.thank_you, name = 'thank_you')
]
