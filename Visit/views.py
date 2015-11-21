from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from ptregister.models import Patient
from doctor_timetable.models import Doctor
from appointment.models import Appointment

import random

# Create your views here.

def index(request):
    return HttpResponse("All Indexes.")

def seed(request):
    d1,xxx=Doctor.objects.get_or_create(
            drusername="tes22t",
            drpassword=make_password(password="test",hasher='sha1'),
            drphone="021234567",
            drname="John",
            drsurname="Smith",
            drsex='m',
            drbirthdate="1990-12-12",
            dridcard="12345617890123",
            draddress="aaa",
            dremail="tes2tt@example.com"
    )
    d1.save()
    d2,xxx=Doctor.objects.get_or_create(
            drusername="t222212",
            drpassword=make_password(password="sdjshdfl",hasher='sha1'),
            drphone="99988877651",
            drname="Doctor",
            drsurname="Karn",
            drsex='f',
            drbirthdate="2004-3-8",
            dridcard="99009902090909",
            draddress="xyz",
            dremail="testx2xxx@new.com"
    )
    d2.save()
    for i in range(0,10) :
        pt = Patient(ptusername=str(random.randrange(1,100)),
        ptpassword=make_password(password=str(random.randrange(0,100000)),hasher='sha1'),
        ptname='name'+str(random.randrange(1,100)),
        ptsurname='sur'+str(random.randrange(1,100)),
        ptsex=random.choice(['M','F']),
        ptbirthdate=str(random.randrange(1,100000)),
        ptidcard=str(random.randrange(1,100)),
        ptaddress=str(random.randrange(1,100)),
        ptemail=str(random.randrange(1,100)),
        ptnum=str(random.randrange(1,100)),
        ptphone=str(random.randrange(1,100)))
        pt.save()
        a = Appointment(doctor=random.choice([d1,d2]), patient=pt, symptom="DiE dIe :) JubJub", cause="StupiD")
        a.save()

    return render(request, 'seed.html')
