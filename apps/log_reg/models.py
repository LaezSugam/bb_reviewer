from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class UserManager(models.Manager):

	def add_user(self, form):
		print form.save()

class User(models.Model):
	name = models.CharField(max_length=255, validators=[MinLengthValidator(2, "Name must be at least 2 characters.")])
	username = models.CharField(max_length=255, validators=[MinLengthValidator(2, "Alias must be at least 2 characters.")])
	email = models.EmailField(max_length=255, unique=True)
	pw_hash = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = UserManager()

	def __str__(self):
		return self.name, self.username, self.email, self.pw_hash
