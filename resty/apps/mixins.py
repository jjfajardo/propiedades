# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


class LoginRequiredMixin(object):
    """
    Este mixin impide que entren a las vistas sin logear
    anteponiendo en nombre del mixin asi
    class AdminList(LoginRequiredMixin, ListView):
    """
    @method_decorator(login_required(login_url="/admin/"))
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class CSRFExemptMixin(object):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(CSRFExemptMixin, self).dispatch(*args, **kwargs)