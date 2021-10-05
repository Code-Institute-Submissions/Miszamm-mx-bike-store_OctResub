from django.urls import path
from .views import (
    HomeView,
    profile,
)
# app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', profile, name='profile'),
]
