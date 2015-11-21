from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest

# Create your views here.
def index(request):
	return render()

def addMedicine(request):
    if request.method == 'POST' :
		name = request.POST["name"]
		table = Medicine.objects.filter(name=name)
		if name is not None and table.count > 0 :
			med = Medicine.objects.create(name=name)
			med.save()
			return render()
		else :
			return render()
def setAvailability(request):
	if request.method == 'POST' :
		name = request.POST["name"]
		availability = request.POST["availability"]
		med = Medicine.objects.get(name=name)
		med.availability = availability
		med.save()
		return HttpResponse('')