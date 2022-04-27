''' Imports needed '''
from django.urls import path
from django.conf.urls.static import static
from . import views
from .webhooks import webhook


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('my_checkout_success/<order_number>', views.my_checkout_success, name='my_checkout_success'
    ),
    path('cache_checkout_data/', views.cache_checkout_data, name='cache_checkout_data'),
    path('wh/', webhook, name='webhook'),
]
