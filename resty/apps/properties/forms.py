__author__ = 'alex'
from django import forms
from .models import House


class FormHouse(forms.ModelForm):
    class Meta:
        model = House
        fields = "__all__"