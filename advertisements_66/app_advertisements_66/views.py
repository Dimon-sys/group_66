from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Advertisement
from .forms import AdvertisementForm

def index(request):
    advertisements = Advertisement.objects.all()
    context = {'advertisements' : advertisements}
    return render(request, 'app_advertisements/index.html', context)

def top_sellers(request):
    return render(request, 'app_advertisements/top-sellers.html')

def advertisement_post(request):
    return render(request, 'app_advertisements/advertisement_post.html')

def register(request):
    return render(request, 'app_auth/register.html')

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

def advertisement(request):
    return render(request, 'app_advertisements/advertisement.html')

def advertisement_post(request):
    if request.method == 'POST':
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = Advertisement(**form.cleaned_data)
            advertisement.user = request.user 
            advertisement.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = AdvertisementForm()
    context = {'form' : form}
    return render(request, 'app_advertisements/advertisement-post.html', context)

# Create your views here.
