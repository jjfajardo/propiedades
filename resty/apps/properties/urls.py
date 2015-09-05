# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import HouseList, AddHouse

urlpatterns = patterns('',
                       url(r'^$', HouseList.as_view(), name="list"),
                       url(r'^add/$', AddHouse.as_view(), name="add"),
                       )
