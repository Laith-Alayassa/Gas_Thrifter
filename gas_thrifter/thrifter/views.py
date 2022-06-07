from tkinter.tix import INTEGER
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import GasPrices

from .forms import GasPricesForm


# Create your views here.
def index(request):
    return render(request, 'thrifter/index.html')

def thank_you(request):
    return render(request, 'thrifter/thank_you.html')

class GasPricesCreateView(CreateView):
    form_class = GasPricesForm
    template_name = "thrifter/create.html"

    success_url = '/thank_you'

    def form_valid(self, form):
        return super().form_valid(form)

def list_view(request):
    max_price = request.GET.get('max_price', '1000')
    object_list = GasPrices.objects.filter(price__lte = float(max_price)).filter(station__contains = request.GET.get('city', ''))
    
    return render(request, 'thrifter/list_view.html', context = {
        'object_list' : object_list
    })