from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime,timedelta

from ptregister.models import Patient
from appointment.models import Appointment
from Visit.models import PatientVisitInfo

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