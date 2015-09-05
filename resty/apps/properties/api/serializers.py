__author__ = 'alex'
from django.contrib.auth.models import User
from rest_framework import serializers
from resty.apps.properties.models import House


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'code', 'name', 'description', 'image', 'latitude', 'longitude', 'price')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')
