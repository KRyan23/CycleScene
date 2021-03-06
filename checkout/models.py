import uuid
# for signals functions
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.db.models import Sum
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField
from products.models import Product
from profiles.models import UserProfile




class Order(models.Model):
    '''This defines the fields required to create an order in the DB'''
    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=30, null=False, blank=False)
    last_name = models.CharField(max_length=30, null=False, blank=False)
    email = models.EmailField(max_length=128, null=False, blank=False)
    mobile_number = models.CharField(max_length=20, null=False, blank=False)
    address1 = models.CharField(max_length=100, null=False, blank=False)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=40, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
    null=True, blank=True, related_name='orders')
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    bag_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_shoppingbag = models.TextField(null=False, blank=False,  default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        '''  Generate a random, unique order number using UUID '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        ''' Update the shopping bag total each time an item is added with delivery cost '''

        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0

        if self.order_total < settings.FREE_DELIVERY_DELTA:
            self.delivery_cost = settings.STANDARD_DELIVERY_COST
        else:
            self.delivery_cost = 0
        self.bag_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        if it hasn't been set already.
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number

class OrderLineItem(models.Model):
    ''' This defines the fields required to create an order line item in the DB '''
    order = models.ForeignKey(Order, null=False, blank=False,
    on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
        max_digits=6, decimal_places=2, null=False, blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the lineitem total
        and update the order total.
        """
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'EAN {self.product.ean} on order {self.order.order_number}'

    def update_total(self):
        ''' Update the shopping bag total each time an item is added with delivery cost '''


# Signal Functions
@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    ''' Update order total on lineitem update/create '''
    instance.order.update_total()

@receiver(post_delete, sender=OrderLineItem)
def update_on_delete(sender, instance, **kwargs):
    ''' Update order total on lineitem delete '''
    instance.order.update_total()
