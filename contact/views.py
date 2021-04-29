from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages


def contact(request):
    return render(request, 'contact.html')
