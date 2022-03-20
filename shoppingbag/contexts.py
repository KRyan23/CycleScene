from django.conf import settings
from decimal import Decimal

def shoppingbag_contents(request):

        ''' Handles the shoppingbag requests '''
        shoppingbag_items = []
        bagtotal = 0
        product_total = 0
        free_delivery = 1

        # Basically dont compare to zero!
        if bagtotal > settings.FREE_DELIVERY_DELTA:
            delivery_local = 0
            delivery_international = 0
            delivery_pickup = 0
            free_delivery = 0
        else:
            delivery_local = bagtotal + Decimal(settings.STANDARD_DELIVERY_COST)
            delivery_international = bagtotal + Decimal(settings.INTERNATIONAL_DELIVERY_COST)
            delivery_pickup = bagtotal * Decimal(settings.LOCAL_PICKUP_COST)
            

            total_bag_cost = bagtotal + delivery_local + delivery_international + delivery_pickup + free_delivery

            context = {
                'shoppingbag_items': shoppingbag_items,
                'bagtotal': bagtotal,
                'product_total': product_total,
                'delivery_local': delivery_local,
                'delivery_international': delivery_international,
                'delivery_pickup': delivery_pickup,
                'free_delivery': free_delivery,
                'total_bag_cost': total_bag_cost,
                'free_delivery_delta': settings.FREE_DELIVERY_DELTA,
            }
            
        return context
