from django.contrib import admin
from .models import OrderItem, Order, BillingAddress
# Register your models here.
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(BillingAddress)
