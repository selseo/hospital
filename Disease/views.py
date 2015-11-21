from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Disease
# Create your views here.
def index(request):
	return render(request,'admin/disease.html',{'table':Disease.objects.all()})

def addDisease(request):
	return HttpResponse('')
#     if request.method == 'POST':
#     	name = request.POST["name"]
#     	ICD10 = request.POST["ICD10"]
#     	if name is not None and ICD10 is not None :
#     		SNOMED = request.POST["SNOMED"]
#     		DRG = request.POST["DRG"]
#     		disease = Disease.objects.create(name=name,ICD10=ICD10,SNOMED=SNOMED,DRG=DRG)
#     		disease.save()
#     		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Success!'}})
# 		else :
# 			return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Fail! Please recheck diseases name and ICD10'})

def setAvailability(request):
	return HttpResponse('')
# 	if request.method == 'POST' :
# 		ICD10 = request.POST["ICD10"]
# 		availability = request.POST["availability"]
# 		med = Medicine.sobjects.get(id=id)
# 		med.availability = availability
# 		med.save()
# 		return HttpResponse('')		