from django.db import models

# Create your models here.
class Client(models.Model):
	ids= models.CharField(max_length=40)
	password= models.CharField(max_length=40)
	def __str__(self):
		return self.ids