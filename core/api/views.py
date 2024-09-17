from rest_framework.viewsets import ModelViewSet
from .serializer import SkipSerializer, CourseSerializer, MyUserSerializer
from home.models import MyUser, Course, Skip
# Create your views here.


class MyUserViewset(ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class CourseViewset(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class SkipViewset(ModelViewSet):
    queryset = Skip.objects.all()
    serializer_class = SkipSerializer