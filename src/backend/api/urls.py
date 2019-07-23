from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.models import User
from django.conf.urls import url
from user import views
from board import views as b_views
# from rest_framework import routers, serializers, viewsets

# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions


urlpatterns = [
    path('index/', b_views.index),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('register/', views.register),
    path('addMessage/', b_views.addMessage),
    path('addvote/', b_views.addVote),
    path('addrefuse/', b_views.addRefuse)
]
