from django.forms import ModelForm
from .models import Item

# Create the form class.


class AdminItemForm(ModelForm):
    class Meta:
        model = Item
        fields = [
            'category', 'sku', 'title', 'price', 'discount_price', 'label', 'slug', 'description',
            'image', 'additional_information'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
