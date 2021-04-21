from django.contrib import admin
from django.urls import path
from .views import item_list

app_name = 'home'

urlpatterns = [
    path('', item_list, name='item-list')
]
