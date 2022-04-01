from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.conf import settings
from shoppingbag.contexts import shoppingbag_contents
from .forms import OrderForm

# Create your views here.



import stripe

# Mostly from BA project
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    
    shoppingbag = request.session.get('shopping_bag', {})
    if not shoppingbag:
        messages.error(request, f"your shopping bag is currently empty!".title())
        return redirect(reverse('home'))

    current_bag = shoppingbag_contents(request)
    total = current_bag['bagtotal']
    stripe_total = round(total * 100)
    stripe.api_key = stripe_secret_key
    intent = stripe.PaymentIntent.create(
        amount=stripe_total,
        currency=settings.STRIPE_CURRENCY,
    )

    print(intent)
    order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'stripe Public key missing check gitpod env also set all ports to public!')
    
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)