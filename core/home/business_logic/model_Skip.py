from django.http import HttpRequest
from home.forms import SkipForm
from home.models import MyUser, Skip
import pandas as pd


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

    skips_data = to_correct_list(request)

    response = set_to_user(skips_data, user)

    return response

        
def to_correct_list(request: HttpRequest):
    try:
        df = pd.read_excel(request.FILES['file_of_skips'])

        skips_data = []

        data = df.values.tolist()

        for item in data:
            print(type(item[2]))
            temp_list = []
            for el in item:
                if isinstance(el, pd.NaT.__class__) or isinstance(el, float):
                    temp_list.append(None)
                else:
                    try:
                        new_date = el.date()
                        temp_list.append(new_date)
                    except:
                        temp_list.append(el)

            skips_data.append(temp_list)


        return skips_data
    
    except:
        return False, 'Пропуски не были добавлены'


def set_to_user(skips_data: list, user: MyUser):

    try:
        for skips in skips_data:
            print(skips)
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
                return False, 'Пропуски не были добавлены'

        return True, 'Пропуски были успешно добавлены'

    except:
        return False, 'Пропуски не были добавлены'
    