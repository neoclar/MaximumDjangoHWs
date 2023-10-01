from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from django.contrib.auth import get_user_model


class UserCreationForm(BaseUserCreationForm):
    username = forms.CharField(label='Никнейм', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    first_name = forms.CharField(label='Имя', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    last_name = forms.CharField(label='Фамилия', max_length=25, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    password1 = forms.CharField(label='Пароль', max_length=25, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control form-control-lg'}))
    password2 = forms.CharField(label='Подтверждение пароля', max_length=25, widget=forms.TextInput(attrs={'type': 'password', 'class': 'form-control form-control-lg'}))
    
    class Meta(BaseUserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name', 'password1', 'password2']
