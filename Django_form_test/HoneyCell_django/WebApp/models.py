from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


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