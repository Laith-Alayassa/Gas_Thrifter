from django.shortcuts import render
from django.views.generic import FormView, CreateView

from .forms import GasPricesForm

# Create your views here.
def index(request):
    return render(request, 'thrifter/index.html')

def thank_you(request):
    return render(request, 'thrifter/thank_you.html')

class GasPricesFormView(CreateView):
    form_class = GasPricesForm
    template_name = "thrifter/form.html"

    success_url = '/thank_you'

    def form_valid(self, form):
        return super().form_valid(form)
