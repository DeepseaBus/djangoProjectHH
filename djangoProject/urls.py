"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# from django.conf.urls import url
# from django.conf.urls import re_path, include
from django.urls import path,re_path,include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics.views import hello_view
from musics import views

router = DefaultRouter()
router.register(r'music', views.MusicViewSet)

handler404 = "djangoProject.views.error_views.view_404"
handler500 = "djangoProject.views.error_views.view_500"

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^hello/', hello_view),
    re_path(r'^api/', include(router.urls)),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]