from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


from datetime import datetime

# Create your models here.


def generate_url(self, filename):
    url = 'documents/%s/%s' %(self.user.username, filename)
    return url

class Book(models.Model):
    user = models.ForeignKey(User)
    book_id = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_description = models.CharField(max_length=100)
    book_file = models.FileField(upload_to=generate_url)


class Memo(models.Model):
    user = models.ForeignKey(User)
    memo_name = models.CharField(max_length=100)
    memo_description = models.TextField(max_length=1000)
    memo_date = models.DateTimeField(default=datetime.now)


class FooModel(models.Model):
    foo_name = models.CharField(max_length=100)
    time_changed = models.DateTimeField(auto_now=True)
    time_created = models.DateTimeField(auto_now_add=True)