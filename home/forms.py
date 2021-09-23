from django.forms import ModelForm
from .models import Item

# Create the form class.
class AdminItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = [
            'category', 'category2', 'sku', 'title', 'price', 'discount_price', 'label', 'slug', 'description',
            'image', 'additional_information'
        ]