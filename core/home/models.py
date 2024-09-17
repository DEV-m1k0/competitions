from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin

# Create your models here.



class Skip(models.Model):
    """
    Модель с пропусками
    """

    title = models.CharField(max_length=100)
    CHOICE = [
        ('Уважительная', 'Уважительная'),
        ('Не уважительная', 'Не уважительная'),
    ]
    cause = models.CharField(max_length=50, choices=CHOICE)
    skip_from = models.DateField(blank=True, null=True)
    skip_to = models.DateField(blank=True, null=True)

    def __str__(self) -> str:
        return str(self.title)
    

CHOICE = [
    ('Администратор системы', "Администратор системы"),
    ('Системный администратор', 'Системный администратор'),
    ('Контент менеджер аппарата управления', 'Контент менеджер аппарата управления'),
    ('Редактор', 'Редактор'),
    ('Пользователь системы', 'Пользователь системы'),
]


class MyUser(AbstractUser, PermissionsMixin):
    """
    Модель пользователей
    """

    role = models.CharField(max_length=50, choices=CHOICE)
    work_number = models.IntegerField(blank=True, null=True)
    home_number = models.IntegerField(blank=True, null=True)
    cabinet = models.IntegerField(blank=True, null=True)
    skip = models.ManyToManyField(Skip, blank=True)
    photo = models.ImageField(upload_to='data/')

    def __str__(self) -> str:
        return str(self.username)
    

class Course(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()

    def __str__(self) -> str:
        return str(self.title)