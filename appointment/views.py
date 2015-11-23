from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .forms import AppForm, AppByStaff

import json
from django.http import JsonResponse
from .models import Department,Dee,timeTable,Appointment
from Authentication.models import Patient, UserProfile, Doctor
from datetime import datetime

import datetime

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
    if request.method == 'POST':
        data = request.POST;
        # save to database
        
        timetable = timeTable.objects.get(id=data.get('appointment'))
        patient = Patient.objects.get(userprofile_id=3)

        newapp = Appointment.objects.create(
            patient_id=patient,
            timetable_id=timetable,
            cause=data.get('cause'),
            symptom=data.get('symptom')
            )

        return HttpResponse('success')
    else:
        form = AppByStaff()
    return render(request, 'appointment/appointmentbystaff.html', {'form': form})


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
    mtimetable = timeTable.objects.filter(doctor_id=doctor, date=d, period='m')
    mpatient = UserProfile.objects.filter(patient__appointment__timetable_id=mtimetable)
    mpatient = serializers.serialize('json', mpatient)

    atimetable = timeTable.objects.filter(doctor_id=doctor, date=d, period='a')
    apatient = UserProfile.objects.filter(patient__appointment__timetable_id=atimetable)
    apatient = serializers.serialize('json', apatient)

    patient = {}
    # patient['a'] = 'a'
    # patient.append({'morning' : mpatient, 'afternoon': apatient})
    patient['morning'] = mpatient
    patient['afternoon'] = apatient
    # patientlist = Appointment.objects.filter(doctor_id=doctor, date__month=month, date__year=year)
    return HttpResponse(json.dumps(patient), content_type='application/json')

def getdoctorlist(request):
    dept = request.GET.get('department')
    doctorlist = UserProfile.objects.filter(doctor__department=dept)
    doctorlist = serializers.serialize('json', doctorlist)
    return HttpResponse(json.dumps(doctorlist), content_type='application/json')

def getappointmentlist(request):
    doc = request.GET.get('doctor')
    timelist = timeTable.objects.filter(doctor_id=doc, date__gte=datetime.date.today()).order_by('date')
    timelist = serializers.serialize('json', timelist)
    return HttpResponse(json.dumps(timelist), content_type='application/json')

def getpatientappointment(request):
    pid = request.POST.get('pid')
    tid = request.POST.get('tid')
    patient = Patient.objects.filter(userprofile_id=pid)
    timetable = timeTable.objects.get(id=tid)
    appointment = Appointment.objects.filter(patient_id=patient, timetable_id=timetable)

    appointment = serializers.serialize('json', appointment)
    patient = serializers.serialize('json', patient)

    result = {}
    result['appointment'] = appointment
    result['profile'] = patient

    return HttpResponse(json.dumps(result), content_type='application/json')    

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

def searchpatient(request):
    pid = request.GET.get('pid')
    pidcard = request.GET.get('pidcard')

    if pidcard == '':
        patient = UserProfile.objects.filter(id=pid)
    else :
        patient = UserProfile.objects.filter(patient__idcard=pidcard)
        
    result = serializers.serialize('json', patient)
    return HttpResponse(result, content_type='application/json') 


def seed(request):
    department = Department.objects.create(name="Anaesthetics")
    department.save()
    department = Department.objects.create(name="Cancer")
    department.save()
    department = Department.objects.create(name="Chaplaincy")
    department.save()
    department = Department.objects.create(name="Gastroenterology")
    department.save()
    # user0,xxx=User.objects.get_or_create(
    #     username="test22t",
    #     defaults={'username':"doctor2",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    # )
    # user0.save()
    # userp0,xxx=UserProfile.objects.get_or_create(
    #     firstname="doctor0",
    #     defaults={'user':user0,'firstname':"WWW",'lastname':"QQQ",'role':1,'status':True}
    # )
    # userp0.save()
    # d1,xxx=Doctor.objects.get_or_create(
    #     department="Cancer",
    #     defaults={'userprofile':userp0, 'department' : 'Cancer'}
    # )
    # d1.save()
    return HttpResponse('Done')