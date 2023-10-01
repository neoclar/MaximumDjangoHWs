from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import UserCreationForm
from .models import RegisterModel

# Create your views here.

def login(request):
    return render(request, 'app_auth/login.html')

@login_required
def profile(request):
    return render(request, 'app_auth/profile.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = RegisterModel(**form.cleaned_data)
            user.save()
            url = reverse('main-page')
            return redirect(url)
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)
