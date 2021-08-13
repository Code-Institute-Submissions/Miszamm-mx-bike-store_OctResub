from django.contrib import admin
from .models import Item, Category
from .models import Carousel

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'title',
        'category',
        'price',
        'label',
        'image'
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_title',
        'title',
   )


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Carousel)
