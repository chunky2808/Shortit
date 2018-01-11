from django.db import models
from django.conf import settings
from .utility import code_generator , create_shortcode
from .validators import validate_url,validate_dot_com
#from django.core.urlresolvers import reverse
#from django_hosts.resolvers import reverse

SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15) # searches in setting for string shortcode_max if it is not there then set it 15

class shortitURLManager(models.Manager):
	def all(self,*args,**kwargs):
		qs_main = super(shortitURLManager,self).all(*args,**kwargs)
		qs = qs_main.filter(active=True)
		return qs

	def refresh_shortcodes(self,items=None):#refresh all short codes
		qs = shortitURL.objects.filter(id__gte=1) #literally all query are here.gte means greater than equal
		if items is not None and isinstance(items ,int):#chceking items is not none and is of type int
			qs = qs.order_by('-id')[:items]#arrange url in ascending order
		new_codes=0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.id)
			q.save()
			new_codes += 1
		return "New codes made: {i}".format(i=new_codes)




class shortitURL(models.Model):
	#inherit from model inheritance
	url = models.CharField(max_length=200, validators = [validate_url,validate_dot_com])
	shortcode = models.CharField(max_length =SHORTCODE_MAX,unique =True,blank = True)
	#shortcode = models.CharField(max_length =15,null = true)empty in database is ok 
	#shortcode = models.CharField(max_length =15,default = 'hiimparas')
	updated = models.DateTimeField(auto_now=True)#everytime model is saved
	timestamp = models.DateTimeField(auto_now_add=True)#when model was created
	#empty_datetime = models.DatetimeField(auto_now = False,auto_now_add = False)
	active  = models.BooleanField(default=True)	
	objects = shortitURLManager()


	def save(self,*args,**kwargs):
		if self.shortcode is None or self.shortcode =="":
			self.shortcode = create_shortcode(self)
		if not "http" in self.url:
			self.url = "http://" + self.url	
		super(shortitURL,self).save(*args,**kwargs) #save it

	def __str__(self):
		return str(self.url) #return string method

	def __unicode__(self):
		return str(self.url)

	def get_short_url(self):
		return "http://127.0.0.1:8000/{shortcode}".format(shortcode=self.shortcode)

