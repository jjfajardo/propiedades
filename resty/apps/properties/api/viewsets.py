__author__ = 'alex'
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import HouseSerializer, UserSerializer
from resty.apps.properties.models import House


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.filter(status=True)
    serializer_class = HouseSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer