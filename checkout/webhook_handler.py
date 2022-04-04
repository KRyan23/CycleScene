from django.http import HttpResponse


class StripeWebhook:
    ''' stripe webhook listener '''

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        ''' handles webhook events '''
        return HttpResponse(
            content=f'Ùnknown Webhook Notification: {event["type"]}',
            status=200)
    
    def handle_payment_intent_succeeded(self, event):
        ''' This is for handling the payment_intent.succeeded webhook '''
        intent = event.data.object
        print(intent)
        return HttpResponse(
            content=f'Success webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
         ''' This is for handling the payment_intent.failed webhook '''
         return HttpResponse(
            content=f'Failure webhook received: {event["type"]}',
            status=200)