from django.shortcuts import render, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail


def contact(request):
    return render(request, 'contact.html')
