from django.http import HttpRequest
from home.models import MyUser

def update_user(request: HttpRequest, user: MyUser):
    try:
        user.first_name=request.POST['first_name']
        user.role = request.POST['role']
        user.work_number=int(request.POST['work_number'])
        user.home_number=int(request.POST['home_number'])
        user.email=request.POST['email']

        user.save()

        return True, 'Пользователь успешно обнавлен'
    
    except:
        return False, 'Пользователь не был обновлен'