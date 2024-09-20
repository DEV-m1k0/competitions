from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from home.models import MyUser
from .forms import MyUserForm, SkipForm, SkipFromExcelForm
from .business_logic import work_with_db


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

    def get(self, request: HttpRequest, id, response: tuple[bool, str] = [None, None], *args: Any, **kwargs: Any) -> HttpResponse: # type: ignore
        user = MyUser.objects.get(id=id)
        skips = user.skip.all()

        role = user.role

        context = {
            'users_editing': user,
            'users': MyUser.objects.filter(role=role),
            'title': role,
            'skips': skips,
            'MyUserForm': MyUserForm,
            'SkipForm': SkipForm,
            'SkipFromExcelForm': SkipFromExcelForm,
            'boolResponse': response[0],
            'textResponse': response[1]
        }

        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request: HttpRequest, id: int):

        response = work_with_db.add_to_db(request, id)

        return self.get(request=request, id=id, response=response)
    

