from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, Carousel


def HomeView(request):
    obj = Carousel.objects.all()
    context = {
        'obj':obj
    }
    return render(request, 'index.html', context)


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Item
    paginate_by = 8
    template_name = "home.html"

    def get_queryset(self):
        category = self.request.GET.get('category')
        if category:
            q = Item.objects.filter(category=category)
        else:
            q = Item.objects.all()
        return q


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"
