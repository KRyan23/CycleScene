''' Imports needed '''
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('my_checkout_success/<order_number>', views.my_checkout_success, name='my_checkout_success'),
]
