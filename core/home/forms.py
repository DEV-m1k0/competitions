from django import forms
from .models import MyUser
from .models import CHOICE


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['photo', 'role', 'work_number', 'home_number', 'email']

        widgets = {
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
            })
        }