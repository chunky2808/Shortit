from django.shortcuts import render,get_object_or_404,Http404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from counter.models import ClickEvent
from .models import shortitURL
from .forms import SubmitUrlForm

#def test_view(requet):
#	return HttpResponse("Some stuff")

# def shortit_redirect_view(request,shortcode =None,*args,**kwargs):#function based view
# 	#print(shortcode)
# 	#obj = shortitURL.objects.get(shortcode = shortcode)
# 	#try:
# 	#	obj = shortitURL.objects.get(shortcode = shortcode)	
# 	#except:
# 	#	obj = shortitURL.objects.all().first()
# 	#print(request.method)
# 	obj = get_object_or_404(shortitURL, shortcode = shortcode)
# 	#obj_url = obj.url
# 	# obj_url = None
# 	# qs = shortitURL.objects.filter(shortcode__iexact=shortcode.upper())
# 	# if qs.exists() and qs.count() == 1:
# 	# 	obj = qs.first()
# 	# 	obj_url = obj.url
# 	return HttpResponseRedirect(obj.url)

def home_view_fbv(request,*args,**kwargs):
 	if request.method == 'POST':
 		print(request.POST)
 	return render(request,"shortener/home.html",{})

class HomeView(View): 	
	def get(self,request,*args,**kwargs):
		the_form = SubmitUrlForm()
		context = {
		"title":"Shortit",
		"form": the_form
		}
		return render(request,"shortener/home.html",context)
	
	def post(self,request,*args,**kwargs):
		form = SubmitUrlForm(request.POST)
		context = {
		"title":"Shortit",
		"form": form
		}
		template = "shortener/home.html"
		if form.is_valid():
			#print(form.cleaned_data.get("url"))
			new_url = form.cleaned_data.get("url")
			obj, created = shortitURL.objects.get_or_create(url=new_url)
			context = {
				"object" :obj,
				"created": created,
			}
			if created:
				template = "shortener/success.html"
			else:
				template = "shortener/already-exists.html"

		# print(request.POST)
		# print(request.POST["url"])
		# print(request.POST.get("url"))
		return render(request,template,context)	


class URLRedirectView(View): # class based view
	def get(self,request,shortcode =None,*args,**kwargs):	
		#print(shortcode)
		qs= shortitURL.objects.filter(shortcode__iexact=shortcode)
		if qs.count()!=1 and not qs.exists():
			raise Http404

		obj = get_object_or_404(shortitURL, shortcode = shortcode)
		print(ClickEvent.objects.create_event(obj))
		return HttpResponseRedirect(obj.url)
	# def post(self,requesst,*args,**kwargs):
	#  	return HttpResponse()
