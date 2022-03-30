from django.contrib import admin
from .models import Order, OrderLineItem
# Register your models here.

class OrderLineItemAdminInline(admin.TabularInline):
    ''' create inline order class inheritable from admin tab inline'''
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)

# Mostly from BA project
class OrderAdmin(admin.ModelAdmin):
    ''' split up the order into editiable and read only fields '''
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'bag_total',)

    fields = ('order_number', 'first_name', 'last_name',
              'email', 'mobile_number', 'address1',
              'address2', 'county', 'city', 'country',
              'postcode', 'date', 'delivery_cost',
              'order_total', 'bag_total',)

    list_display = ('order_number', 'date', 'first_name', 'last_name',
                    'order_total', 'delivery_cost',
                    'bag_total',)

    ordering = ('-date',)


admin.site.register(Order, OrderAdmin)