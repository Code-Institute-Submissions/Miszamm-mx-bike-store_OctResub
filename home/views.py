from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from django.utils import timezone
from .models import Item, Carousel


def products(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, "products.html", context)


class HomeView(ListView):
    model = Carousel
    template_name = "home.html"

    def get_queryset(self):
        return Carousel.objects.filter(is_active=True).all()


class ItemDetailView(DetailView):
    model = Item
    template_name = "product.html"


class ShopView(ListView):
    model = Item
    paginate_by = 8
    template_name = "shop.html"

    def get_queryset(self):
        category = self.request.GET.get('category')
        q = Item.objects.all()
        if category:
            q = q.filter(category=category)
        search = self.request.GET.get('search')
        if search:
            q = q.filter(title__icontains=search)
        return q
