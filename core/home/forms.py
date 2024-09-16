from django import forms
from .models import MyUser


class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['skip']