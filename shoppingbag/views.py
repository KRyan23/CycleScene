from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
# Create your views here.

def view_shoppingbag(request):
    """ renders the shopping bag template  """

    
    return render(request, 'shoppingbag/shoppingbag.html')