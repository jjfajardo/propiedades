__author__ = 'alex'
from django.views.generic import View
from django.http import JsonResponse
from resty.apps.properties.models import House
from resty.apps.mixins import LoginRequiredMixin


class ValidateCode(LoginRequiredMixin, View):

    def post(self, request):
        print(request.POST)
        if 'house_code' in request.POST and request.POST['house_code']:
            try:
                house = House.objects.get(code=request.POST['house_code'])
            except:
                house = None
            if house:
                my_json = {'available': False}
            else:
                my_json = {'available': True}
        else:
            my_json = {'error': True}
        return JsonResponse(my_json, safe=True)
