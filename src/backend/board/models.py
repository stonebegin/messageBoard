from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.CharField(max_length=128)
    body = models.TextField()
    created_time = models.CharField(max_length=256)
    tag = models.IntegerField(default=0)
    good = models.IntegerField(default=0)
    bad = models.IntegerField(default=0)

    def __str__(self):
        return self.author