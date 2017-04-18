from django.conf.urls import include, url
from django.contrib import admin
from reg_sub.views import *
urlpatterns = [
    url(r'^$', home),
]
