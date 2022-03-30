from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from . forms import OrderForm

# Mostly from BA project
def checkout(request):
    shoppingbag = request.session.get('shopping_bag', {})
    if not shoppingbag:
        messages.error(request, f"your shopping bag is currently empty!".title())
        return redirect(reverse('home'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
    }

    return render(request, template, context)