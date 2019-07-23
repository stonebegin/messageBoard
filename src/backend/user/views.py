from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
# import logging
import json
from .models import User
def index(request):
    pass
    return HttpResponse("index")

def login(request):
    if request.method == 'POST':
        # logging.debug(request.POST)
        username = request.POST.get('username', None)
        password = request.POST.get('passwd', None)
        if username and password:
            username = username.strip()
            try:
                user = User.objects.filter(username=username)
                sendData = json.loads(serializers.serialize('json', user, ensure_ascii=False))
            except:
                return HttpResponse('connect db failed')
            if sendData[0]['fields']['passwd'] == password:
                return HttpResponse("userpass")
        return HttpResponse("NO!!!")

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        email = request.POST.get('email')
        user = User(
            username=username,
            passwd=password,
            email=email
        )
        user.save()
        
    return HttpResponse("registersuccess")
