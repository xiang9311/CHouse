__author__ = '祥祥'

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'index/$', views.index, name='index'),
]