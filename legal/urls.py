'''Required Imports'''
from django.urls import path
from . import views


urlpatterns = [
    path('', views.view_legal, name='legal'),
]
