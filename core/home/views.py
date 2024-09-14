from typing import Any
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import MyUser

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        context['admin_sys'] = MyUser.objects.filter(role='Администратор системы')
        context['sys_admin'] = MyUser.objects.filter(role='Системный администратор')

        return context