from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
# Create your views here.

def view_shoppingbag(request):
    """ renders the shopping bag template  """

    
    return render(request, 'shoppingbag/shoppingbag.html')

def add_product_to_shoppingbag(request, item_id):
    ''' Adds products to shopping bag function '''
    
    bag_quantity = request.POST.get('quantity')
    print(bag_quantity)
    bag_quantity = int(bag_quantity)
    current_page = request.POST.get('current_page_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
       shopping_bag[item_id] += bag_quantity
    else:
        shopping_bag[item_id] = bag_quantity

    request.session['shopping_bag'] = shopping_bag
    print(request.session['shopping_bag'])
    return redirect(current_page)