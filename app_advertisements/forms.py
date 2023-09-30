from django import forms
from .models import Advertisement

class Advertisementform(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(forms.ModelForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['description'].widget = forms.Textarea(attrs={'class': 'form-control form-control-lg'})
        self.fields['price'].widget = forms.NumberInput(attrs={'class': 'form-control form-control-lg'})
        self.fields['auction'].widget = forms.CheckboxInput(attrs={'class': 'form-check-input'})
        self.fields['image'].widget = forms.FileInput(attrs={'class': 'form-control form-control-lg'})

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']

# Старый класс
# class Advertisementform(forms.Form):
#     title = forms.CharField(max_length=64, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
#     price = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
#     auction = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
#     image = forms.ImageField(required=False, widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))