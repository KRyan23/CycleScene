'''cyclescene URL Configuration'''

import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('shoppingbag/', include('shoppingbag.urls')),
    path('checkout/', include('checkout.urls')),
    path('legal/', include('legal.urls')),
    path('service/', include('service.urls')),
    path('profile/', include('profiles.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = "cyclescene.views.page_not_found"
handler400 = "cyclescene.views.bad_request"
handler500 = "cyclescene.views.internal_server_error"
