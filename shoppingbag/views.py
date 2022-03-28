''' Imports needed '''
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages
from products.models import Product

def view_shoppingbag(request):
    ''' renders the shopping bag template '''
    return render(request, 'shoppingbag/shoppingbag.html')


def add_product_to_shoppingbag(request, item_id):
    ''' Adds products to shopping bag function '''
    product = Product.objects.get(pk=item_id)
    bag_quantity = request.POST.get('quantity')
    bag_quantity = int(bag_quantity)
    current_page = request.POST.get('current_page_url')
    shopping_bag = request.session.get('shopping_bag', {})
    messages.add_message(request, messages.INFO, 'added to your bag')
    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += bag_quantity
    else:
        shopping_bag[item_id] = bag_quantity
    request.session['shopping_bag'] = shopping_bag
    return redirect(current_page)


def changebag_quantity(request, item_id):
    """ Change the quantity of an item in the shopping bag """

    quantity = int(request.POST.get('quantity'))

    shopping_bag = request.session.get('shopping_bag', {})
    if quantity > 0 or quantity < 11:
        messages.add_message(request, messages.INFO, 'Quantity Changed')
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shoppingbag'))


def delete_items_from_shoppingbag(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)
        request.session['shopping_bag'] = shopping_bag
        messages.add_message(request, messages.INFO, 'Item removed from bag!')
        return HttpResponse(status=200)

    except Exception as e:
        return HttpResponse(status=500)
