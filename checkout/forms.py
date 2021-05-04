from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget



class CheckoutForm(forms.Form):
    street_addres = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '123 Main St'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Site or appartment'
    }))
    country = CountryField(blank_label='(select country)').formfield(
        widget=CountrySelectWidget(attrs={
            'class': 'custom-select d-block w-100'
        }))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_shipping_address = forms.BooleanField(required=False)
    save_info = forms.BooleanField(required=False)
    
