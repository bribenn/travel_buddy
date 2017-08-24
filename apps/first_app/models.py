from __future__ import unicode_literals

from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
	def validateUser(self, post_data):

		is_valid = True
		errors = []
		#first name must be greater than 2 characters
		if len(post_data.get('first_name')) < 2:
			is_valid = False
			errors.append('first name must be more than 2 characters')
		#last name must be more than 2 characters
		if len(post_data.get('last_name')) < 2:
			is_valid = False
			errors.append('last name must be more than 2 characters')
		#if email is valid
		if not re.search(r'\w+\@\w+.\w+', post_data.get('email')):
			is_valid = False
			errors.append('must enter a valid email')
		#if password >= 8 characters, matches password confirmation
		if len(post_data.get('password')) < 8:
			is_valid = False
			errors.append('password must be at least 8 characters')
		if post_data.get('password_confirmation') != post_data.get('password'):
			is_valid = False
			errors.append('password and password confirmation must match')

		return (is_valid, errors)

class User(models.Model):
	first_name = models.CharField(max_length = 45)
	last_name = models.CharField(max_length = 45)
	email = models.CharField(max_length = 100)
	password = models.CharField(max_length = 255)
	friends = models.ManyToManyField("self")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)
	objects = UserManager()

class Message(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, related_name="author")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)

class Note(models.Model):
	content = models.CharField(max_length=45)
	user = models.ForeignKey(User, related_name="notes")

class Trip(models.Model):
	destination = models.CharField(max_length = 255)
	details = models.TextField()
	start_date = models.DateField(auto_now_add=False)
	end_date = models.DateField(auto_now_add=False)
	creator = models.ForeignKey(User, related_name="created_trips")
	participants = models.ManyToManyField(User, related_name="joined_trips")
	messages = models.ForeignKey(Message, related_name="messages")
	notes = models.ForeignKey(Note, related_name="notes")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)


class Comment(models.Model):
	content = models.TextField()
	author = models.ForeignKey(User, related_name="comments")
	replies = models.ManyToManyField("self")
	message = models.ForeignKey(Message, related_name="comments")
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now_add = True)





