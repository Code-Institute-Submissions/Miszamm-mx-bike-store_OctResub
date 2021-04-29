from django import forms
from django_countries.fields import CountryField


class CheckoutForm(forms.Form):
    street_addres = forms.CharField(max_length=40, null=True, blank=True)
    apartment_address = forms.Charfield(required=False)
    country = CountryField(blank_label='(select country)')
    postcode = forms.CharField(max_length=20, null=True, blank=True)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
