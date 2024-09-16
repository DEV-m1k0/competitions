"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from home.views import HomeView, HomeUsersView, HomeUsereditingView
from api import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.MyUserViewset, basename='my_users_api')
router.register(r'courses', views.CourseViewset, basename='course_api')
router.register(r'skips', views.SkipViewset, basename='skips_api')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('users/<int:id>/', HomeUsersView.as_view(), name='user_by_id'),
    path('user/editing/<int:id>', HomeUsereditingView.as_view(), name='user_editing'),
    path('api/', include(router.urls)),
    path('', include('rest_framework.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
