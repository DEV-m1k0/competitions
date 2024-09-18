from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from home.models import MyUser, Skip
from .forms import MyUserForm, SkipForm

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


        user = MyUser.objects.get(id=id)
        skips = user.skip.all()

        role = user.role

        context = {
            'users_editing': user,
            'users': MyUser.objects.filter(role=role),
            'title': role,
            'skips': skips,
            'MyUserForm': MyUserForm,
            'SkipForm': SkipForm
        }

        return render(request=request, template_name=self.template_name, context=context)
    
    def post(self, request: HttpRequest, id):

        # print(request.POST)
        # print(request.POST['first_name'])


        try:
            user = MyUser.objects.get(id=id)

            user.first_name=request.POST['first_name']
            user.role = request.POST['role']
            user.work_number=int(request.POST['work_number'])
            user.home_number=int(request.POST['home_number'])
            user.email=request.POST['email']

            user.save()

        except:
            form = SkipForm(request.POST)

            if form.is_valid():
                skip = form.save()
                user.skip.add(skip)


        return self.get(request=request, id=id)