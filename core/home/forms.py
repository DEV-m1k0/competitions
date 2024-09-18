from django import forms
from .models import MyUser, Skip
from .models import CHOICE


class SkipForm(forms.ModelForm):
    class Meta:
        model = Skip
        fields = "__all__"

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control my-1'
            }),
            'skip_from': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control my-1'
            }),
            'skip_to': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control my-1'
            }),
            'cause': forms.Select(attrs={
                'class': 'form-control my-1',

            }, choices=[
        ('Уважительная', 'Уважительная'),
        ('Не уважительная', 'Не уважительная'),
    ])
        }


class MyUserForm(forms.ModelForm):

    name_and_middlename = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'd-none',
        'id': 'inputNameAndMiddlename'
    }))
    
    class Meta:
        model = MyUser
        fields = ['photo', 'first_name', 'role', 'work_number', 'home_number', 'email']

        widgets = {
            'photo': forms.FileInput(attrs={
                'class': 'd-none',
                'id': 'inputFile'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'd-none',
                'id': 'inputUsername'
            }),
            'role': forms.Select(attrs={
                'class': 'btn btn-light d-none',
                'id': 'selectRole'
            }, choices=CHOICE),
            'work_number': forms.TextInput(attrs={
                'class': 'd-none',
                'id': 'inputWorkNumber',
            }),
            'home_number': forms.TextInput(attrs={
                'class': 'd-none',
                'id': 'inputHomeNumber',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'd-none',
                'id': 'inputEmail',
            })
        }