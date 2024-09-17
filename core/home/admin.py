from django.contrib import admin
from .models import MyUser, Skip, Course

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Skip)
admin.site.register(Course)