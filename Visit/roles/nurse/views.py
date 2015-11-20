from django.http import HttpResponse
from django.shortcuts import render

from ptregister.models import Patient
from appointment.models import Appointment

# Create your views here.

def index(request):
	return render(request, 'nurse/index.html')
def view(request):
	return render(request, 'nurse/view.html',{'table':Appointment.objects.all()})