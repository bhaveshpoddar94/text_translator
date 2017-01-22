from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TimeStampedModel(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	class Meta:
		abstract = True

class Translation(TimeStampedModel):
	text = models.TextField(default="UNKNOWN")
	translatedText = models.TextField(default="UNKNOWN")
	toLangCode = models.CharField(max_length=50)
	fromLangCode = models.CharField(max_length=50)
	error = models.BooleanField(default=False)
