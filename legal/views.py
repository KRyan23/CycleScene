'''Required Imports'''
from django.shortcuts import render
from .models import Legal

def view_legal(request):
    """ A view to show individual legal details """
    legal = Legal.objects.all()
    context = {
        'legal': legal
    }
    return render(request, 'legal/legal.html', context)
