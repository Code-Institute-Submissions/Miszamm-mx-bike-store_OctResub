from django.shortcuts import render
from .models import Carousel
# Create your views here.


def index(request):
    """ Aview to return the index page """
    obj = Carousel.objects.all()
    context = {
        'obj': obj
    }
    return render(request, 'home/index.html', context)
