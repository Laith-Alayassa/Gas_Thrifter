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

class GasPricesFormListView(ListView):
    model = GasPrices
    template_name = 'thrifter/list_view.html'

    def get_queryset(self):
        queryset = super().get_queryset()


    def get_queryset(self):
        filter_val = self.request.GET.get('price_filter', 0)
        print(f'this is the filter value ============ {filter_val}')
        new_context = GasPrices.objects.filter(price=filter_val)
        return new_context

    def get_context_data(self, **kwargs):
        context = super(GasPricesFormListView, self).get_context_data(**kwargs)
        context['price_filter'] = self.request.GET.get('price_filter', 2)