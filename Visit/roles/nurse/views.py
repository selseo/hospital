from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta

from ptregister.models import Patient
from appointment.models import Appointment
from Visit.models import PatientVisitInfo
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PatientVisitForms
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def index(request):
	return render(request, 'nurse/index.html')
def view(request):
	return render(request, 'nurse/view.html',{'table':PatientVisitInfo.objects.filter(
		 lastUpdate__day=datetime.now().day,
		 lastUpdate__month=datetime.now().month,
		 lastUpdate__year=datetime.now().year,
		 status=0
	)})

@csrf_exempt
def edit(request,num):
	instance = get_object_or_404(PatientVisitInfo, appointment_id=num)
	form = PatientVisitForms(request.POST or None, instance=instance)
	if form.is_valid:
		form.save()
		return render(request, 'nurse/edit.html', {'num':num})
	return render(request, 'nurse/edit.html', {'num':num})