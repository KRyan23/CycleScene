''' Required Imports '''
from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    '''Register and displays all fields in the correct order for the various 'service' sections'''
    list_display = (
        'name',
        'titlerepair',
        'bodyrepair',
        'titlerescue',
        'bodyrescue',
        'service1',
        'service2'
    )

    ordering = ('name', 'titlerepair', 'bodyrepair', 'titlerescue',
    'bodyrescue', 'service1', 'service2')

admin.site.register(Service, ServiceAdmin)
