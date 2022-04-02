''' Imports needed '''
from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product
from django.contrib import messages

def shoppingbag_contents(request):

    ''' Handles the shoppingbag requests '''
    shoppingbag_items = []
    bagtotal = 0
    total_bag_cost = 0
    product_total = 0
    product_count = 0
    free_delivery = 1
    delivery = 0
    mybag = request.session.get('shopping_bag', {})

    for item_id, quantity in mybag.items():
        product = get_object_or_404(Product, pk=item_id)
        bagtotal += quantity * product.price
        product_total += quantity
        shoppingbag_items.append({
                'item_id': item_id,
                'quantity': quantity,
                'product': product,
            })

    if bagtotal > settings.FREE_DELIVERY_DELTA:
        total_bag_cost = bagtotal * free_delivery
    else:
        total_bag_cost = bagtotal + Decimal(settings.STANDARD_DELIVERY_COST)
        delivery = delivery + Decimal(settings.STANDARD_DELIVERY_COST)
       
    context = {
                'shoppingbag_items': shoppingbag_items,
                'bagtotal': bagtotal,
                'product_total': product_total,
                'product_count': product_count,
                'free_delivery': free_delivery,
                'total_bag_cost': total_bag_cost,
                'free_delivery_delta': settings.FREE_DELIVERY_DELTA,
                'delivery': delivery,
            }
    return context
