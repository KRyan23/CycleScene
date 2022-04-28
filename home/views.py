from django.shortcuts import render

# Create your views here.

def index(request):
    """ Loads index.html from the home app """
    return render(request, 'home/index.html')
