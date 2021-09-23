from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.shortcuts import redirect
from .models import Item, Carousel
from checkout.forms import CheckoutForm
from checkout.models import BillingAddress
from django.forms.models import model_to_dict

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView


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


def profile(request):
    try:
        billing_address = BillingAddress.objects.get(user=request.user)
        initial_data = model_to_dict(billing_address)
    except BillingAddress.DoesNotExist:
        billing_address = None
        initial_data = {}
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            street_address = form.cleaned_data.get('street_address')
            city = form.cleaned_data.get('city')
            county = form.cleaned_data.get('county')
            country = form.cleaned_data.get('country')
            zip = form.cleaned_data.get('zip')
            if billing_address:
                billing_address.first_name = first_name
                billing_address.last_name = last_name
                billing_address.street_address = street_address
                billing_address.city = city
                billing_address.county = county
                billing_address.country = country
                billing_address.zip = zip
            else:
                billing_address = BillingAddress(
                        first_name=first_name,
                        last_name=last_name,
                        street_address=street_address,
                        city=city,
                        county=county,
                        country=country,
                        zip=zip,
                        user=request.user
                        )
            billing_address.save()
            return redirect('profile')
    form = CheckoutForm(initial=initial_data)
    context = {
       'form': form
    }
    return render(request, "home/profile.html", context)

 
class AdminProductList(ListView):
    model = Item
    paginate_by = 8
    template_name = "admin_product_list.html"


class AdminProductCreateView(CreateView):
    model = Item
    fields = [
            'category', 'sku', 'title', 'price', 'discount_price', 'label', 'slug', 'description',
            'image', 'additional_information'
        ]
    template_name = "admin_product_create.html"
    success_url = reverse_lazy('admin_product_list')

class AdminProductUpdateView(UpdateView):
    model = Item
    fields = [
            'category', 'sku', 'title', 'price', 'discount_price', 'label', 'slug', 'description',
            'image', 'additional_information'
        ]
    template_name = "admin_product_create.html"
    success_url = reverse_lazy('admin_product_list')

class AdminProductDeleteView(DeleteView):
    model = Item
    template_name = "admin_product_delete.html"
    success_url = reverse_lazy('admin_product_list')