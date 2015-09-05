# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url, include
from .views import HouseList, AddHouse
from .webservices import urls as url_ws
from api.router import properties_router


urlpatterns = patterns('',
                       url(r'^api/', include(properties_router.urls)),  # <- Rest properties
                       url(r'^$', HouseList.as_view(), name="list"),
                       url(r'^add/$', AddHouse.as_view(), name="add"),
                       url(r'ws/', include(url_ws, namespace='ws')),
                       )
