from django.urls import path
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.view_shoppingbag, name='view_shoppingbag'),
    path('add/<item_id>', views.add_product_to_shoppingbag, name='add_product_to_shoppingbag'),
]
