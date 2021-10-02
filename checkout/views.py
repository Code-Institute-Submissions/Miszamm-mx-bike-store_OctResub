from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.views.generic import View
from django.shortcuts import redirect
from django.utils import timezone
from .models import OrderItem, Order, BillingAddress
from home.models import Item
from .forms import CheckoutForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.forms.models import model_to_dict


class CheckoutView(View):
    def get(self, *args, **kwargs):
        try:
            billing_address = BillingAddress.objects.get(user=self.request.user)
            initial_data = model_to_dict(billing_address)
        except BillingAddress.DoesNotExist:
            billing_address = None
            initial_data = {}
        order = Order.objects.filter(user=self.request.user, ordered=False).first()
        form = CheckoutForm(use_required_attribute=False, initial=initial_data)
        context = {
            'form': form,
            'object': order,
        }
        return render(self.request, "checkout.html", context)

    def post(self, *args, **kwargs):
        try:
            billing_address = BillingAddress.objects.get(user=self.request.user)
        except BillingAddress.DoesNotExist:
            billing_address = None
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'form': form,
                'object': order,
            }
            if form.is_valid():
                first_name = form.cleaned_data.get('first_name')
                last_name = form.cleaned_data.get('last_name')
                street_address = form.cleaned_data.get('street_address')
                city = form.cleaned_data.get('city')
                county = form.cleaned_data.get('county')
                country = form.cleaned_data.get('country')
                zip = form.cleaned_data.get('zip')
                # Functionality for those fields needs to be added
                #   same_shipping_address = form.cleaned_data.get(
                #       'same_shipping_address')
                #   save_info = form.cleaned_data.get('save_info')
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
                            # user=request.user,
                            )
                billing_address.save()
                order.billing_address = billing_address
                order.save()
                return redirect('payment')
            print(form.errors)
            messages.warning(self.request, "Failed checkout")
            # return redirect('checkout')
            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("order-summary")


class PaymentView(View):
    def get(self, *args, **kwargs):
        return render(self.request, "payment.html")


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object': order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an active order")
            return redirect("/")


@login_required
def add_to_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    quantity = int(request.GET.get('quantity', 1))
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            cart_item = order.items.get(item__slug=item.slug)
            cart_item.quantity += quantity
            cart_item.save()
            messages.info(request, "Item quantity was updated succesfully")
            return redirect("order-summary")
        else:
            order_item, created = OrderItem.objects.get_or_create(
                item=item,
                user=request.user,
                ordered=False,
                quantity=quantity
            )
            order.items.add(order_item)
            messages.info(request, "Item was added to your cart succesfully")
            return redirect("order-summary")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order_item, created = OrderItem.objects.get_or_create(
            item=item,
            user=request.user,
            ordered=False,
            quantity=quantity
        )
        order.items.add(order_item)
        messages.info(request, "Item was remove from cart succesfully")
        return redirect("order-summary")


def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            elif order_item.quantity == 1:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("product", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("product", slug=slug)


@login_required
def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            messages.info(
                request, "Item was removed from your cart sucesfully")
            return redirect("order-summary")
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("order-summary")
    else:
        messages.info(request, "You do not have an active order")
        return redirect("order-summary")


class SuccessView(View):
    def get(self, *args, **kwargs):
        session_id = self.request.GET.get('session_id')
        session = stripe.checkout.Session.retrieve(session_id)
        customer = stripe.Customer.retrieve(session.customer)
        order = Order.objects.get(user=self.request.user, ordered=False)
        order.ordered = True
        order.save()
        context = {
            'object': order,
            'customer_email': customer.email
        }
        return render(self.request, "success.html", context)


import os

import stripe


# This is your real test secret API key.
stripe.api_key = 'sk_test_51IUTHGAWMAUBj98U84CnKpfmV44EmBSxWGQAVeuwDr0ECfVlvdT9ImT3ZSdtfnRVtDwx6iCUxnEt0twSXu9lu1Th002CTlLLDB'


@csrf_exempt
def create_checkout_session(request):
    order = Order.objects.get(user=request.user, ordered=False)
    line_items = []
    for item in order.items.all():
        order_item = {
            'price_data': {
                'currency': 'usd',
                'unit_amount': int(item.item.price * 100),
                'product_data': {
                    'name': item.item.title,
                    'images': [request.build_absolute_uri(settings.MEDIA_URL + str(item.item.image))],
                },
            },
            'quantity': item.quantity,
        }
        line_items.append(order_item)
    try:
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=line_items,
            mode='payment',
            success_url=settings.SITE_DOMAIN + '/checkout/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=settings.SITE_DOMAIN + '/cancel.html',
        )
        return JsonResponse({'id': checkout_session.id})
    except Exception as e:
        return JsonResponse({'error': str(e)})
