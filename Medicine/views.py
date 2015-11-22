from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Medicine
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
@csrf_exempt
def index(request):
	return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})

@csrf_exempt
def addMedicine(request):
    if request.method == 'POST':
    	name = request.POST["name"]
    	table = Medicine.objects.filter(name=name)
    	if name and (table.count()==0):
    		med = Medicine.objects.create(name=name)
    		med.save()
    		return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'message':"Add Medicine Success!",'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})
    	else:
    		return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'message':"Add Medicine Fail! Please recheck your medicine's name.",'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})
@csrf_exempt
def setAvailability(request):
	name = request.POST["name"]
	availability = request.POST["availability"]
	if availability == "true":
		med = Medicine.objects.get(name=name)
		med.availability = True
		med.save()
	else : 
		med = Medicine.objects.get(name=name)
		med.availability = False
		med.save()
	return HttpResponse('')