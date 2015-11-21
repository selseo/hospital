from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Disease
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
@csrf_exempt
def index(request):
	return render(request,'admin/disease.html',{'table':Disease.objects.all(),'length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})
@csrf_exempt
def addDisease(request):
    if request.method == 'POST':
    	name = request.POST["name"]
    	ICD10 = request.POST["ICD10"]
    	if name and ICD10:
    		SNOMED = request.POST["SNOMED"]
    		DRG = request.POST["DRG"]
    		disease = Disease.objects.create(name=name,ICD10=ICD10,SNOMED=SNOMED,DRG=DRG)
    		disease.save()
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Success!','length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})
    	else :
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Fail! Please recheck diseases name and ICD10','length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})

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