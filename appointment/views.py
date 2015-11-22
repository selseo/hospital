from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .forms import AppForm

import json
from django.http import JsonResponse
from .models import Department,Dee,Doctor,timeTable,Appointment
from Authentication.models import UserProfile
from datetime import datetime

#for restframework
from rest_framework import viewsets
from .serializers import DepartmentSerializer, DeeSerializer
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#for restframework
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeeViewset(viewsets.ModelViewSet):
    queryset = Dee.objects.all()
    serializer_class = DeeSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def doctor(request):
    return HttpResponse(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

def show(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            
            data = {'form': form.cleaned_data , 'hello': 'world'}
            return HttpResponse(json.dumps(data), content_type='application/json')

            # redirect to a new URL:
            #return HttpResponseRedirect('/app/')
        return HttpResponse("Fake save : Invalid Form Input!")
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppForm()
        department = Department.objects.all()

    return render(request, 'appointment/appointment.html', {'department': department,'form':form})

def appointmentbystaff(request):
    return render(request, 'appointment/appointmentbystaff.html', {'appointment': []})


def editappointment(request):
    return render(request, 'appointment/edit_appointment.html', {'appointment': []})

def editappointmentbystaff(request):
    return render(request, 'appointment/edit_appointmentbystaff.html', {'appointment': []})


def reschedule(request, aid):
    return render(request, 'appointment/reschedule.html', {'appointment': []})


def cancel(request, aid):
    return render(request, 'appointment/cancel.html', {'appointment': []})


def patientlist(request):
    return render(request, 'appointment/patientlist.html')

def getpatientlist(request):
    # this below line should be replaced with session
    doctor = Doctor.objects.get(id=1)
    # Prepare data
    year = request.GET.get('year')
    month = request.GET.get('month')
    date = request.GET.get('date')
    # move below line to manager class
    availableDate = str(date)+"-"+str(month)+"-"+str(year)    
    d = datetime.strptime(availableDate, "%d-%m-%Y")

    # get timetable first to refer appointment
    timetable = timeTable.objects.filter(doctor_id=doctor, date=d)
    # patient = Patient.appointment_set.filter(timetable_id=timetable)
    patient = UserProfile.objects.filter(appointment__timetable_id=timetable)
   
    # patientlist = Appointment.objects.filter(doctor_id=doctor, date__month=month, date__year=year)
    result = serializers.serialize('json', patient)
    return HttpResponse(result, content_type='application/json')

def timetable(request):
    return render(request, 'appointment/timetable.html')

def savetimetable(request):
    availables = json.loads(request.POST.get('availables'))
    year = request.POST.get('year')
    month = request.POST.get('month')
    for available in availables:
        # Preparing and preprocessing data
        availableDate = str(available['date'])+"-"+str(month)+"-"+str(year)    
        d = datetime.strptime(availableDate, "%d-%m-%Y")
        # this below line must be replaced with session data
        doctor = Doctor.objects.get(id=1)

        # Call TimetableManager to edit timetable
        timeTable.objects.editTimetable(doctor=doctor, d=d, available=available)

    #return success
    return HttpResponse('success')

@csrf_exempt
def gettimetable(request):
    # this below line should be replaced with session
    doctor = Doctor.objects.get(id=1)
    year = request.GET.get('year')
    month = request.GET.get('month')
    time = timeTable.objects.filter(doctor_id=doctor, date__month=month, date__year=year)
    for t in time :
        t.date = t.date.day
    result = serializers.serialize('json', time)
    return HttpResponse(result, content_type='application/json')


def seedDoctor(request):
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
    return HttpResponse('done')

def seedPatient(request):
# 0|id|integer|1||1
# 1|firstname|varchar(50)|1||0
# 2|lastname|varchar(50)|1||0
# 3|role|integer|1||0
# 4|status|integer|1||0
# 5|user_id|integer|1||0
# 6|idcard|varchar(20)|1||0
# 7|phone|varchar(15)|1||0
# 8|sex|varchar(1)|1||0
    p = UserProfile.objects.create(
        user_id='1',
        firstname="John",
        lastname="Doe",
        sex="m",
        idcard="1234567890123",
        phone="9999999999",
        role="2"
        )
    p.save()
    return HttpResponse('done')

def seedAppointment(request):
    # 0|id|integer|1||1
    # 1|patient_id_id|integer|1||0
    # 2|timetable_id_id|integer|1||0
    # 3|symptom|varchar(100)|1||0
    # 4|cause|varchar(100)|1||0
    patient=UserProfile.objects.get(user_id=1)
    timetable=timeTable.objects.all()[0]
    a = Appointment.objects.create(
        patient_id=patient,
        timetable_id=timetable,
        symptom='symptom',
        cause='cause'
        )
    a.save()
    return HttpResponse('done')