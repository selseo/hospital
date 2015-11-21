from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest

# Create your views here.
def index(request):
	return render()

def addDisease(request):
    if request.method == 'POST' :
		name = request.POST["name"]
		ICD10 = request.POST["ICD10"]
		if name is not None and ICD10 is not None : 
			SNOMED = request.POST["SNOMED"]
			DRG = request.POST["DRG"]
			disease = Disease.objects.create(name=name,ICD10=ICD10,SNOMED=SNOMED,DRG=DRG)
			disease.save()
			return render()
		else :
			return render()
def setAvailability(request):
	if request.method == 'POST' :
		id = request.POST["id"]
		availability = request.POST["availability"]
		med = Medicine.sobjects.get(id=id)
		med.availability = availability
		med.save()
		return HttpResponse('')		