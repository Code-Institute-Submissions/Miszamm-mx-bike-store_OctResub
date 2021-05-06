from django.shortcuts import render   
from django.core.mail import send_mail


def contact(request):
    send_mail(
        'Subject here',
        'Here is the message.',
        'miszamm@zohomail.eu',
        ['c00242566@itcarlow.ie'],
        fail_silently=False,
    )
    return render(request, 'contact.html')
