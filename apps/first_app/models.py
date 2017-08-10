from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 100)
	password = models.CharField(max_length = 255)
	trips = models.ManyToManyField(Trip, related_name="trips", default=None)
	friends = models.ManyToManyField("self")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)
