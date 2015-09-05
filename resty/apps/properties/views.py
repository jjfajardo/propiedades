from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import ListView, View
from .models import House
from .forms import FormHouse
from resty.apps.mixins import LoginRequiredMixin


class HouseList(LoginRequiredMixin, ListView):
    template_name = "index.html"
    model = House


class AddHouse(LoginRequiredMixin, View):
    template_name = "add.html"
    form = FormHouse

    def get(self, request):
        return render(request, self.template_name, {'form': self.form})

    def post(self, request):
        my_form = self.form(request.POST, request.FILES)
        if my_form.is_valid():
            new_house = my_form.save(commit=False)
            new_house.save()
            return HttpResponseRedirect("/")
        return render(request, self.template_name, {'form': my_form})
