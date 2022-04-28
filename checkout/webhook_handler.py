''' Required Imports '''
import json
import time
from django.http import HttpResponse
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from products.models import Product
from profiles.models import UserProfile
from .models import Order, OrderLineItem

class StripeWebhook:
    ''' stripe webhook listener '''

    def __init__(self, request):
        self.request = request
    # From BA project
    def _send_confirmation_email(self, order):
        ''' This is to send the user a confirmation email '''
        send_customer_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confimation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confimation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL })

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [send_customer_email]
        )


    def handle_event(self, event):
        ''' handles most webhook events '''
        return HttpResponse(
            content=f'Ùnknown Webhook Notification: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        shoppingbag = intent.metadata.shoppingbag
        save_info = intent.metadata.save_info

        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update the users profile information if the 'save info' checkbox is ticked.

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_mobile_number=shipping_details.mobile_number
                profile.default_country=shipping_details.address.country
                profile.default_postcode=shipping_details.address.postcode
                profile.default_city=shipping_details.city
                profile.default_address1=shipping_details.address1
                profile.default_address2=shipping_details.address2
                profile.default_county=shipping_details.county
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    mobile_number__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county__iexact=shipping_details.address.state,
                    bag_total=grand_total,
                    original_shoppingbag=shoppingbag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                content=
                f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    first_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    mobile_number=shipping_details.phone,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county=shipping_details.address.state,
                    original_shoppingbag=shoppingbag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(shoppingbag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()

            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        ''' This is for handling the payment_intent.failed webhook '''
        return HttpResponse(
            content=f'Failure webhook received: {event["type"]}',
            status=200)
