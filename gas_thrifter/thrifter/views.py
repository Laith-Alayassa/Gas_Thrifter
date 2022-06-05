from tkinter.tix import INTEGER
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from .models import GasPrices

from .forms import GasPricesForm


def is_valid_queryparam(param):
    return param != '' and param is not None



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

# class GasPricesFormListView(ListView):
#     model = GasPrices
#     template_name = 'thrifter/list_view.html'

#     def get_queryset(self):
#         queryset = super().get_queryset()


#     def get_queryset(self):
#         filter_val = self.request.GET.get('price_filter', 0)
#         print(f'this is the filter value ============ {filter_val}')
#         new_context = GasPrices.objects.filter(price=filter_val)
#         return new_context

#     def get_context_data(self, **kwargs):
#         context = super(GasPricesFormListView, self).get_context_data(**kwargs)
#         context['price_filter'] = self.request.GET.get('price_filter', 2)
    
# def list_view_filtered(request, max_price = 100):
#     print('reached filtered view')
#     max_price = float(request.GET['max_price'])

#     object_list = GasPrices.objects.filter(price__lte = float(max_price))
#     return render(request, 'thrifter/list_view.html', context = {
#         'object_list' : object_list
#     })

def list_view(request):
    object_list = GasPrices.objects.all()
    max_price = request.GET.get('max_price', '')
    if is_valid_queryparam(max_price):
        object_list = GasPrices.objects.filter(price__lte = float(max_price))
    
    return render(request, 'thrifter/list_view.html', context = {
        'object_list' : object_list
    })