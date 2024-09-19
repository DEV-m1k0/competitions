from django.http import HttpRequest
from home.forms import SkipForm
from home.models import MyUser, Skip
import pandas as pd
from datetime import datetime


def add_skip(request: HttpRequest, user: MyUser):
    try:
        form = SkipForm(request.POST)

        if form.is_valid():
            skip = form.save()
            user.skip.add(skip)

        return True, 'Пропуск успешно добавлен'

    except:
        return False, 'Пропуск не был добавлен'
    


def add_skip_from_excel(request: HttpRequest, user: MyUser):
    df = pd.read_excel(request.FILES['file_of_skips'])


    skips_data = []

    data = df.values.tolist()

    for item in data:
        temp_list = []
        for el in item:
            if el is pd.NaT:
                temp_list.append(None)
            else:
                try:
                    new_date = el.date()
                    temp_list.append(new_date)
                except:
                    temp_list.append(el)

        skips_data.append(temp_list)


    for skips in skips_data:
        
        try:
            skip = Skip.objects.create(
                title=skips[0],
                skip_from=skips[1],
                skip_to=skips[2],
                cause=skips[3]
            )

            try:
                user.skip.add(skip)
            except:
                print('Пропуск пользователю не добавлен')

        except:
            print('Пропуск не создался')

        
