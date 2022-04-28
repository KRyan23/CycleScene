''' Required Imports '''
from django.shortcuts import render
from .models import Service

def view_service(request):
    """ A view to show the bulk of the individual service page details """
    service = Service.objects.all()
    context = {
        'service': service
    }
    return render(request, 'service/service.html', context)
