'''Required Imports'''
from django.urls import path
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.view_legal, name='legal'),
]
