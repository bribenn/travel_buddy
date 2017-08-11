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

class Trip(models.Model):
	destination = models.CharFeild(max_length = 255)
	details = models.TextField()
	start_date = models.DateField(auto_now_add=False)
	end_date = models.DateField(auto_now_add=False)
	creator = models.ForeignKey(User, related_name="created_trips")
	participants = models.ForeignKey(User, related_name="participants")
	messages = models.ForeignKey(Message, related_name="messages")
	notes = models.ForeignKey(Note, related_name="notes")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Message(models.Model):
	content = models.TextField()
	comments = models.ForeignKey(Comment, related_name="comments")
	author = models.ForeignKey(User, related_name="author")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Comment(models.Model):
	content = models.TextFeild()
	author = models.ForeignKey(User, related_name="author")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Note(models.Model):
	content = models.CharField(max_length=45)




