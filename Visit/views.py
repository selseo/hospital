from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password

from ptregister.models import Patient
from appointment.models import Appointment

import random

# Create your views here.

def index(request):
    return HttpResponse("All Indexes.")

def seed(request):
    d1=Doctor.objects.create(
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
        d1.save()
    d2=Doctor.objects.create(
            drusername="t2222",
            drpassword=make_password(password="sdjshdfl",hasher='sha1'),
            drphone="99988877651",
            drname="Doctor",
            drsurname="Karn",
            drsex='f',
            drbirthdate="2004-3-8",
            dridcard="9900990090909",
            draddress="xyz",
            dremail="testxxxx@new.com"
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
        ptphone=str(random.randrange(1,100)),)
	    pt.save()

	return render(request, 'seed.html')
