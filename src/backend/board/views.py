from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from .models import Post
# import logging

def index(request):
    # logging.debug("index success")
    tmp_data = Post.objects.all().order_by('-created_time')
    post_list = serializers.serialize('json', tmp_data, ensure_ascii=False)
    return HttpResponse(post_list)

def addMessage(request):
    # logging.debug("add mess request success")
    username = request.POST.get('username')
    body = request.POST.get('content')
    created_time = request.POST.get('created_time')
    tag = request.POST.get('tag')
    user = Post(
        author=username,
        created_time=created_time,
        body=body,
        tag=tag
    )
    user.save()
    
    return HttpResponse("messagesuccess")

def addVote(request):
    # logging.debug("add vote request success")
    author = request.POST.get('author')
    good = request.POST.get('good')
    created_time = request.POST.get('created_time')
    post = Post.objects.get(author=author,created_time=created_time)
    post.good = good
    post.save()
    
    return HttpResponse("votesuccess")

def addRefuse(request):
    # logging.debug("add refuse request success")
    author = request.POST.get('author')
    bad = request.POST.get('bad')
    created_time = request.POST.get('created_time')
    post = Post.objects.get(author=author,created_time=created_time)
    post.bad = bad
    post.save()
    
    return HttpResponse("refusesuccess")