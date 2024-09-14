from django.db import models

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

class User(models.Model):
    """
    Модель пользователей
    """

    CHOICE = [
        ('Администратор системы', "Администратор системы"),
        ('Системный администратор', 'Системный администратор'),
        ('Контент менеджер аппарата управления', 'Контент менеджер аппарата управления'),
        ('Редактор', 'Редактор'),
        ('Пользователь системы', 'Пользователь системы')
    ]
    role = models.CharField(max_length=50, choices=CHOICE)
    name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    work_number = models.IntegerField()
    home_number = models.IntegerField(blank=True, null=True)
    email = models.EmailField()
    cabinet = models.IntegerField()
    skip = models.ManyToManyField(Skip, blank=True)
    photo = models.ImageField(upload_to='data/')

    def __str__(self) -> str:
        return f'{self.name} {self.middle_name} {self.last_name}'
    

class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=100)
    start = models.DateField()
    end = models.DateField()