from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
# From BA project
from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    ''' Update order total on lineitem update/create '''
    print("signal issueed post_save")
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    ''' Update order total on lineitem delete '''
    print("signal issueed post_dalate")
    instance.order.update_total()