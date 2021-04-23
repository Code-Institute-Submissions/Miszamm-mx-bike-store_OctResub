from django.contrib import admin
from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    checkout
)


app_name = 'home'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ItemDetailView.as_view(), name='product'),
    path('checkout/', checkout, name='checkout')
]
