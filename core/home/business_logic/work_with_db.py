from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from .model_MyUser import update_user
from home.models import MyUser
from .model_Skip import add_skip, add_skip_from_excel


def add_to_db(request: HttpRequest, id: int):
    user = MyUser.objects.get(id=id)

    type_data = check_data(request)

    print(type_data)

    response = {
        "update_user": update_user(request, user),
        "add_skip": add_skip(request, user),
        'file_of_skips': add_skip_from_excel(request, user)
    }[type_data]

    return response


def check_data(request: HttpRequest):
    if 'first_name' in request.POST and 'role' in request.POST:
        return 'update_user'
    
    elif 'skip_from' in request.POST and 'skip_to' in request.POST:
        return 'add_skip'
    
    elif 'file_of_skips' in request.POST or 'file_of_skips' in request.FILES:
        return 'file_of_skips'







