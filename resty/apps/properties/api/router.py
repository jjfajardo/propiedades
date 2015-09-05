__author__ = 'alex'
from rest_framework import routers
from .viewsets import HouseViewSet, UserViewSet

properties_router = routers.DefaultRouter()
properties_router.register(r'houses', HouseViewSet)
properties_router.register(r'users', UserViewSet)

