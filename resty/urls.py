from django.conf.urls import include, url
from django.contrib import admin
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('resty.apps.properties.urls', namespace="properties")),
    url(r'^api/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': MEDIA_ROOT}),
]
