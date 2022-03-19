from django.shortcuts import render

# Create your views here.

def view_shoppingbag(request):
    """ renders the shopping bag template  """
    return render(request, 'shoppingbag/shoppingbag.html')