from django.conf.urls import url
from django.contrib import admin

from .views import shrink_url, redirect

urlpatterns = [
    url(r'^$', shrink_url, name='shrink_url'),
    url(r'^(?P<id>\w+)/$', redirect, name='redirect'),
]
