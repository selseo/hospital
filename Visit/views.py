from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from datetime import datetime,timedelta

from Authentication.models  import Patient
from appointment.models import Doctor,timeTable
from appointment.models import Appointment
from Visit.models import PatientVisitInfo

import random

# Create your views here.
# please remove comment syntax to use authen

def index(request):
    #if request.user.is_authenticated():
        #if getUserProfile(request.user).role==2:
            return HttpResponse("All Indexes.")
        #else :
            #return HttpResponseRedirect('/default/')
    #else :
        #return HttpResponseRedirect('/default/')

def seed(request):
<<<<<<< HEAD
    #if request.user.is_authenticated():
        #if getUserProfile(request.user).role==2:
            d1,xxx=Doctor.objects.get_or_create(
                    drusername="tes22t",
                    defaults={'drpassword':make_password(password="test",hasher='sha1'),
                    'drphone':"021234567",
                    'drname':"John",
                    'drsurname':"Smith",
                    'drsex':'m',
                    'drbirthdate':"1990-12-12",
                    'dridcard':"12345617890123",
                    'draddress':"aaa",
                    'dremail':"tes2tt@example.com"}
            )
            d1.save()
            t11,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t11.save()
            t12,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t12.save()
            t13,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t13.save()
            t14,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t14.save()
            t15,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t15.save()
            d2,xxx=Doctor.objects.get_or_create(
                    drusername="t22,xxx2212",
                    defaults={'drpassword':make_password(password="sdjshdfl",hasher='sha1'),
                    'drphone':"99988877651",
                    'drname':"Doctor",
                    'drsurname':"Karn",
                    'drsex':'f',
                    'drbirthdate':"2004-3-8",
                    'dridcard':"99009902090909",
                    'draddress':"xyz",
                    'dremail':"testx2xxx@new.com"}
            )
            d2.save()
            t21,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t21.save()
            t22,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t22.save()
            t23,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t23.save()
            t24,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t24.save()
            t25,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
            t25.save()
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
                a = Appointment(timetable_id=random.choice([t11,t12,t13,t14,t15,t21,t22,t23,t24,t25,]), patient_id=pt, symptom="DiE dIe :) JubJub", cause="StupiD")
                a.save()
                v = PatientVisitInfo(appointment=a,
            weight=str(random.randrange(50,100)),
            height=str(random.randrange(100,200)),
            pulse=str(random.randrange(40,120)),
            systolic=str(random.randrange(50,110)),
            diastolic=str(random.randrange(100,200)),
            status=str(random.randrange(0,4)),
            note=str(random.randrange(13,103452350)),)
                v.save()
                PatientVisitInfo.objects.filter(appointment=a).update(lastUpdate=v.lastUpdate-timedelta(hours=random.randrange(0,200)))
            return render(request, 'seed.html')
        #else :
            #return HttpResponseRedirect('/default/')
    #else :
        #return HttpResponseRedirect('/default/')
=======
    d1,xxx=Doctor.objects.get_or_create(
            drusername="tes22t",
            defaults={'drpassword':make_password(password="test",hasher='sha1'),
            'drphone':"021234567",
            'drname':"John",
            'drsurname':"Smith",
            'drsex':'m',
            'drbirthdate':"1990-12-12",
            'dridcard':"12345617890123",
            'draddress':"aaa",
            'dremail':"tes2tt@example.com"}
    )
    d1.save()
    t11,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t11.save()
    t12,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t12.save()
    t13,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t13.save()
    t14,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t14.save()
    t15,xxx=timeTable.objects.get_or_create(doctor_id=d1,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t15.save()
    d2,xxx=Doctor.objects.get_or_create(
            drusername="t22,xxx2212",
            defaults={'drpassword':make_password(password="sdjshdfl",hasher='sha1'),
            'drphone':"99988877651",
            'drname':"Doctor",
            'drsurname':"Karn",
            'drsex':'f',
            'drbirthdate':"2004-3-8",
            'dridcard':"99009902090909",
            'draddress':"xyz",
            'dremail':"testx2xxx@new.com"}
    )
    d2.save()
    t21,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t21.save()
    t22,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t22.save()
    t23,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t23.save()
    t24,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t24.save()
    t25,xxx=timeTable.objects.get_or_create(doctor_id=d2,date=datetime.now()-timedelta(hours=random.randrange(-200,200)),period=random.choice(['m','a']),)
    t25.save()
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
        a = Appointment(timetable_id=random.choice([t11,t12,t13,t14,t15,t21,t22,t23,t24,t25,]), patient_id=pt, symptom="DiE dIe :) JubJub", cause="StupiD")
        a.save()
        v = PatientVisitInfo(appointment=a,
    weight=str(random.randrange(50,100)),
    height=str(random.randrange(100,200)),
    pulse=str(random.randrange(40,120)),
    systolic=str(random.randrange(50,110)),
    diastolic=str(random.randrange(100,200)),
    status=str(random.randrange(0,4)),
    note=str(random.randrange(13,103452350)),)
        v.save()
        PatientVisitInfo.objects.filter(appointment=a).update(lastUpdate=v.lastUpdate-timedelta(hours=random.randrange(0,50)))
    return render(request, 'seed.html')
>>>>>>> ec5044a242551cbecb207c67cf07c56909cfe8e9
