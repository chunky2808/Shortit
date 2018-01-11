from django.db import models

# Create your models here.
from shortener.models import shortitURL

class ClickEventManager(models.Manager):
	def create_event(self,shortitintance):
		if isinstance(shortitintance,shortitURL):
			obj,created = self.get_or_create(shortit_Url=shortitintance)
			obj.count +=1
			obj.save()
			return obj.count
		return None	

class ClickEvent(models.Model):
	shortit_Url = models.OneToOneField(shortitURL)
	count = models.IntegerField(default=0)
	updated = models.DateTimeField(auto_now=True)#everytime model is saved
	timestamp = models.DateTimeField(auto_now_add=True)#when model was created
	
	objects = ClickEventManager()

	def __str__(self):
		return "{i}".format(i=self.count)