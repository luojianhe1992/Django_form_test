from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


from datetime import datetime

# Create your models here.


def generate_url_documents(self, filename):
    url = 'documents/%s/%s' %(self.user.username, filename)
    return url

def generate_url_images(self, filename):
    url = 'images/%s/%s' %(self.user.username, filename)
    return url

class Book(models.Model):
    user = models.ForeignKey(User)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_description = models.CharField(max_length=100)
    book_file = models.FileField(upload_to=generate_url_documents)


class Memo(models.Model):
    user = models.ForeignKey(User)
    memo_name = models.CharField(max_length=100)
    memo_description = models.TextField(max_length=1000)
    memo_datetime = models.DateTimeField(default=datetime.now)


class FooModel(models.Model):
    foo_name = models.CharField(max_length=100)
    time_changed = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)



class Picture(models.Model):
    user = models.ForeignKey(User)
    picture_name = models.CharField(max_length=100)
    picture_image = models.ImageField(upload_to=generate_url_images)
    picture_time_created = models.DateTimeField(auto_now_add=True)
    picture_time_changed = models.DateTimeField(auto_now=True)