from django.conf.urls import include, url
from django.contrib import admin
from apps.properties import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('resty.apps.properties.urls', namespace="properties")),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework'))
]
