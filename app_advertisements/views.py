from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from .models import Advertisement
from .forms import Advertisementform
# Create your views here.

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements': advertisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = Advertisementform(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = Advertisementform()
    context = {'form': form}
    return render(request, 'app_advertisements/advertisement-post.html', context)
# HttpResponse('Успешное подключение!')
