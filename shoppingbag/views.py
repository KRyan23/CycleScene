from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
# Create your views here.

def view_shoppingbag(request):
    """ renders the shopping bag template  """
    return render(request, 'shoppingbag/shoppingbag.html')


def add_product_to_shoppingbag(request, item_id):
    ''' Adds products to shopping bag function '''
    
    bag_quantity = request.POST.get('quantity')
    bag_quantity = int(bag_quantity)
    current_page = request.POST.get('current_page_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += bag_quantity
    else:
        shopping_bag[item_id] = bag_quantity

    request.session['shopping_bag'] = shopping_bag
    return redirect(current_page)
    

def changebag_quantity(request, item_id):
    """ Change the quantity of an item in the shopping bag """

    quantity = request.POST.get('quantity')
    quantity = int(quantity)

    if quantity > 0 or quantity < 11:
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_shoppingbag'))
