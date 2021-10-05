from django.shortcuts import render
from django.views.generic import ListView, DetailView, View
from home.models import Item
from .forms import AdminItemForm
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# Create your views here.


class ItemDetailView(DetailView):
    model = Item
    template_name = "products/product.html"


class ShopView(ListView):
    model = Item
    paginate_by = 8
    template_name = "products/shop.html"

    def get_queryset(self):
        category = self.request.GET.get('category')
        q = Item.objects.all()
        if category:
            q = q.filter(category=category)
        search = self.request.GET.get('search')
        if search:
            q = q.filter(title__icontains=search)
        return q


class AdminProductList(ListView):
    model = Item
    paginate_by = 8
    template_name = "products/admin_product_list.html"


class AdminProductCreateView(CreateView):
    model = Item
    template_name = "products/admin_product_create.html"
    success_url = reverse_lazy('admin_product_list')
    form_class = AdminItemForm


class AdminProductUpdateView(UpdateView):
    model = Item
    template_name = "products/admin_product_create.html"
    success_url = reverse_lazy('admin_product_list')
    form_class = AdminItemForm


class AdminProductDeleteView(DeleteView):
    model = Item
    template_name = "products/admin_product_delete.html"
    success_url = reverse_lazy('admin_product_list')
    form_class = AdminItemForm
