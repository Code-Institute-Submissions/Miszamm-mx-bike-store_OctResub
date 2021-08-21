from django.urls import path
from .views import (
    HomeView,
    ItemDetailView,
    ShopView,
    profile,
)
# app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('shop', ShopView.as_view(), name='shop'),
    path('product/<slug>', ItemDetailView.as_view(), name='product'),
    path('profile/', profile, name='profile'),
]
