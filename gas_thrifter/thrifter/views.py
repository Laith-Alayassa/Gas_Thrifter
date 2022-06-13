
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import CreateView, ListView
from django.contrib.auth.forms import UserCreationForm
from .models import GasPrices
from django.contrib.auth import login


from .forms import GasPricesForm


# Create your views here.
def index(request):
    if request.POST:
        city = request.POST.get('location')
        return redirect('thrifter:list_view', city=city)
    else:
        if request.user.is_authenticated:    
            return render(request, 'thrifter/index.html', context= {
                'authenticated' : True
            })
        else:
            return render(request, 'thrifter/index.html', context= {
                'authenticated' : False
            })

def thank_you(request):
    return render(request, 'thrifter/thank_you.html')


class GasPricesCreateView(CreateView):
    form_class = GasPricesForm
    template_name = "thrifter/create.html"

    success_url = '/thank_you'

    def form_valid(self, form):
        return super().form_valid(form)


def list_view(request, city=''):
    max_price = request.GET.get('max_price', 1000) if request.GET.get(
        'max_price', 100.0) is not '' else 1000

    city = request.POST.get(
        'location', '') if request.POST else request.GET.get('city', '')

    object_list = GasPrices.objects.filter(
        price__lte=float(max_price)).filter(city__city__contains=city)

    return render(request, 'thrifter/list_view.html', context={
        'object_list': object_list
    })


# class signupView(CreateView):
#     # form_class = UserCreationForm


#     form_class = NewUserForm
#     template_name = 'registration/signup.html'
    
#     success_url = '/'




def station_map(request, station):
    a=station
    return render(request, 'thrifter/map.html')



def register(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # login(request,)
        else:
            return render(request, 'registration/signup.html', context = {'form' : form})

    form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'registration/signup.html', context = context)