from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse 
from django.core.urlresolvers import reverse
from django.views import generic
from doctor_timetable.models import Doctor,timeTable
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
import math
import json
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
# this file was copied from doctor_timetable without editing anythings - if any, pls delete this line and add new comment
def index(request):
	doctor = Doctor.objects.filter(drusername="test")
	if doctor.count()==0:
		doctor=Doctor.objects.create(
			drusername="test",
			drpassword=make_password(password="test",hasher='sha1'),
			drphone="021234567",
			drname="John",
			drsurname="Smith",
			drsex='m',
			drbirthdate="1990-12-12",
			dridcard="1234567890123",
			draddress="aaa",
			dremail="test@example.com"
		)
		doctor.save()
	time = timeTable.objects.filter(dr=doctor)
	return render(request, 'doctor_patient_list/index.html',{'doctor':doctor,'time':time})


def getData(request):
	doctor = Doctor.objects.get(drusername="test")
	time = timeTable.objects.filter(dr=doctor, date__month=request.GET.get('month'), date__year=request.GET.get('year'))
	for t in time :
		t.date = t.date.day
	time2 = serializers.serialize('json', time)
	return HttpResponse(time2, content_type='application/json')

def getData2(request):
	doctor = Doctor.objects.get(drusername="test")
	time = timeTable.objects.filter(dr=doctor, date__month=request.GET.get('month'), date__year=request.GET.get('year'))
	for t in time :
		t.date = t.date.day
	time2 = serializers.serialize('json', time)
	return HttpResponse(time2, content_type='application/json')
	