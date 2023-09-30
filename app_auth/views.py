from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'app_auth/login.html')

def profile(request):
    return render(request, 'app_auth/profile.html')

def register(request):
    return render(request, 'app_auth/register.html')
