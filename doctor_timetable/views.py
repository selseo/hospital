from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect,HttpResponse 
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Doctor,timeTable
from django.contrib.auth.hashers import make_password
from datetime import datetime
from django.http import JsonResponse
from django.core import serializers
import math
import json
# Create your views here.

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
	return render(request, 'doctor_timetable/index.html',{'doctor':doctor,'time':time})

from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def save(request):
	data = json.loads(request.POST['slist'])

	for i in data:
		currentDate = str(i['date'])+"-"+str(request.POST['month'])+"-"+str(request.POST['year'])
		Date = datetime.strptime(currentDate, "%d-%m-%Y")
		doctor = Doctor.objects.get(drusername="test")
		table = timeTable.objects.filter(dr=doctor,date=Date)

		if table.count()==1:
			table = timeTable.objects.get(dr=doctor,date=Date)
			if i['period']==0:
				if i['status']==1:
					table.time1 = True;
					table.save()
				else :
					table.time1 = False;
					table.save()
			else :
				if i['status']==1 :
					table.time2 = True;
					table.save()
				else :
					table.time2 = False;
					table.save()
			
		else :
			if i['period']==0:
				if i['status']==1 :
					time1 = True;
					time2 = False;
					table = timeTable.objects.create(dr=doctor,date=Date,time1=time1,time2=time2,patientnum=0)
					table.save()
				else :
					time1 = False;
					time2 = False;
					table = timeTable.objects.create(dr=doctor,date=Date,time1=time1,time2=time2,patientnum=0)
					table.save()
			else :
				if i['status']==1 :
					time1 = False;
					time2 = True;
					table = timeTable.objects.create(dr=doctor,date=Date,time1=time1,time2=time2,patientnum=0)
					table.save()
				else :
					time1 = False;
					time2 = False;
					table = timeTable.objects.create(dr=doctor,date=Date,time1=time1,time2=time2,patientnum=0)
					table.save()
			
			
	return HttpResponse('')
def getData(request):
	doctor = Doctor.objects.get(drusername="test")
	time = timeTable.objects.filter(dr=doctor, date__month=request.GET.get('month'), date__year=request.GET.get('year'))
	for t in time :
		t.date = t.date.day
	time2 = serializers.serialize('json', time)
	return HttpResponse(time2, content_type='application/json')
	