from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Medicine
# Create your views here.
def index(request):
	return render(request,'index.html',{'table':Medicine.objects.all()})

def addMedicine(request):
    if request.method == 'POST' :
		name = request.POST["name"]
		table = Medicine.objects.filter(name=name)
		if name is not None and table.count > 0 :
			med = Medicine.objects.create(name=name)
			med.save()
			return render(request,'index.html',{'table':Medicine.objects.all(),'message':"Add Medicine Success!"})
		else :
			return render(request,'index.html',{'table':Medicine.objects.all(),'message':"Add Medicine Fail! Please recheck your medicine's name."})
def setAvailability(request):
	if request.method == 'POST' :
		name = request.POST["name"]
		availability = request.POST["availability"]
		med = Medicine.objects.get(name=name)
		med.availability = availability
		med.save()
		return HttpResponse('')