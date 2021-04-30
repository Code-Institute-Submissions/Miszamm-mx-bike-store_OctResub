from django import forms
from django_countries.fields import CountryField


PAYMENT_CHOICES = {
    ('S', 'Stripe'),
    ('P', 'PayPal')
}


class CheckoutForm(forms.Form):
    street_addres = forms.CharField(max_length=40)
    apartment_address = forms.CharField(required=False)
    country = CountryField(blank_label='(select country)')
    postcode = forms.CharField(max_length=20)
    same_billing_address = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.BooleanField(widget=forms.RadioSelect())
    save_info = forms.BooleanField(widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(
        widget=forms.RadioSelect(choices=PAYMENT_CHOICES))
