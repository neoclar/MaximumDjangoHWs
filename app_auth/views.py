from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import ExtendedUserCreationForm
# from .models import RegisterModel

# Create your views here.

def login(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return redirect(redirect_url)
    return render(request, 'app_auth/register.html', {'error': 'Такой пользователь не найден!'})

@login_required(login_url=reverse_lazy('login'))
def profile(request):
    return render(request, 'app_auth/profile.html')

def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        if form.is_valid():
            # user = RegisterModel(**form.cleaned_data)
            # user.save()
            user = form.save()
            user = authenticate(username=user.username, password=request.POST['password1'])
            login(request, user=user)
            return redirect(reverse('profile'))
            # url = reverse('main-page')
            # return redirect(url)
    else:
        form = ExtendedUserCreationForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)

def logout(request):
    logout(request)
    return redirect(reverse('login'))