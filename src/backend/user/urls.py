from django.urls import path
# from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('', views.register, name='register'),
    path('', views.logout, name='logout'),
    path('', views.index, name='index')
]