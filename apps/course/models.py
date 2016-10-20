from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Courses(models.Model):
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)


class Descriptions(models.Model):
	description = models.TextField(max_length=400)
	course_id = models.OneToOneField(Courses)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)	
