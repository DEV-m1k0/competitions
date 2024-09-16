from rest_framework.serializers import ModelSerializer
from home import models


class MyUserSerializer(ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = '__all__'



class SkipSerializer(ModelSerializer):
    class Meta:
        model = models.Skip
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model = models.Course
        fields = '__all__'

