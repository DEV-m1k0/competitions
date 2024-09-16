from typing import Any
from django.http import HttpRequest
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
    

class HomeUsersView(TemplateView):
    def get(self, request: HttpRequest, id: int, *args: Any, **kwargs: Any) -> HttpResponse:

        role = {
            0: 'Администратор системы',
            1: 'Системный администратор',
            2: 'Контент менеджер аппарата управления',
            3: 'Редактор',
            4: 'Пользователь системы'
        }[id]

        context = {
            'users': MyUser.objects.filter(role=role),
            'title': role
        }

        return render(request=request, template_name='home.html', context=context)
    

class HomeUsereditingView(TemplateView):
    template_name = 'home.html'

    def get(self, request: HttpRequest, id, *args: Any, **kwargs: Any) -> HttpResponse:

        role = {
            1: 'Администратор системы',
            2: 'Системный администратор',
            3: 'Контент менеджер аппарата управления',
            4: 'Редактор',
            5: 'Пользователь системы'
        }[int(request.get_full_path()[-1])]

        context = {
            'users_editing': MyUser.objects.filter(id=id),
            'users': MyUser.objects.filter(role=role),
            'title': role,
        }

        return render(request=request, template_name=self.template_name, context=context)