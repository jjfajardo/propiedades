# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from .views import ValidateCode

urlpatterns = patterns('',
                       url(r'^validate/code/$', ValidateCode.as_view(), name="code"),
                       )