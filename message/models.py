from django.db import models
from django.utils import timezone


class Message(models.Model):

	sender = models.CharField(max_length=200)
	reciever = models.CharField(max_length=200)
	message = models.TextField(null=True)
	create_datetime = models.DateTimeField(default=timezone.now)




