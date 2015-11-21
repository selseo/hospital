from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.hashers import make_password
from .forms import AppForm

import json
from django.http import JsonResponse
from .models import Department,Dee,Doctor,timeTable
from Authentication.models  import Patient
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
    doctor = Doctor.objects.filter(drusername="test")
    
    time = timeTable.objects.filter(doctor_id=doctor)
    return render(request, 'appointment/patientlist.html',{'doctor':doctor,'time':time})

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
        doctor = Doctor.objects.get(drusername="test")

        # Call TimetableManager to edit timetable
        timeTable.objects.editTimetable(doctor=doctor, d=d, available=available)

    #return success
    return HttpResponse('success')

@csrf_exempt
def gettimetable(request):
    # this below line should be replaced with session
    doctor = Doctor.objects.get(drusername="test")
    year = request.GET.get('year')
    month = request.GET.get('month')
    time = timeTable.objects.filter(doctor_id=doctor, date__month=month, date__year=year)
    for t in time :
        t.date = t.date.day
    result = serializers.serialize('json', time)
    return HttpResponse(result, content_type='application/json')