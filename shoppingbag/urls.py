''' Imports needed '''
from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.view_shoppingbag, name='view_shoppingbag'),
    path('add/<item_id>', views.add_product_to_shoppingbag, name='add_product_to_shoppingbag'),
    path('adjust/<item_id>/', views.changebag_quantity, name='changebag_quantity'),
    path('remove/<item_id>/', views.delete_items_from_shoppingbag,
    name='delete_items_from_shoppingbag'),
]
