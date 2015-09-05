__author__ = 'alex'
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import HouseSerializer, UserSerializer
from resty.apps.properties.models import House
from rest_framework import permissions


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.filter(status=True)
    serializer_class = HouseSerializer
    permission_classes = (permissions.AllowAny, )


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated, )
