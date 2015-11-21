from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Disease
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
<<<<<<< HEAD
# please remove comment syntax to use authen
def index(request):
	#if request.user.is_authenticated():
        #if getUserProfile(request.user).role==5:
			return render(request,'admin/disease.html',{'table':Disease.objects.all()})
		#else :
            #return HttpResponseRedirect('/default/')
    #else :
        #return HttpResponseRedirect('/default/')

=======
@csrf_exempt
def index(request):
	return render(request,'admin/disease.html',{'table':Disease.objects.all()})
@csrf_exempt
>>>>>>> ec5044a242551cbecb207c67cf07c56909cfe8e9
def addDisease(request):
    if request.method == 'POST':
    	name = request.POST["name"]
    	ICD10 = request.POST["ICD10"]
    	if name and ICD10:
    		SNOMED = request.POST["SNOMED"]
    		DRG = request.POST["DRG"]
    		disease = Disease.objects.create(name=name,ICD10=ICD10,SNOMED=SNOMED,DRG=DRG)
    		disease.save()
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Success!'})
    	else :
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Fail! Please recheck diseases name and ICD10'})

@csrf_exempt
def setAvailability(request):
	# return HttpResponse('')
	
	ICD10 = request.POST["ICD10"]
	availability = request.POST["availability"]
	print (availability)
	if availability == "true":
		di = Disease.objects.get(ICD10=ICD10)
		di.availability = True
		di.save()
	else : 
		di = Disease.objects.get(ICD10=ICD10)
		di.availability = False
		di.save()

	# .update(availability=availability)
	# print (di.availability)
	# di.availability = availability
	# di.save()
	# di = Disease.objects.filter(ICD10=ICD10)
	# res = serializers.serialize('json',di)
	return HttpResponse('')		
