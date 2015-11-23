from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.hashers import make_password
from datetime import datetime,timedelta
from django.contrib.auth.models import User

from Authentication.models  import Patient,UserProfile, Doctor
from appointment.models import timeTable,Appointment
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
    #if request.user.is_authenticated():
        #if getUserProfile(request.user).role==2:
            # d1,xxx=Doctor.objects.get_or_create(
            #         drusername="tes22t",
            #         defaults={'drpassword':make_password(password="test",hasher='sha1'),
            #         'drphone':"021234567",
            #         'drname':"John",
            #         'drsurname':"Smith",
            #         'drsex':'m',
            #         'drbirthdate':"1990-12-12",
            #         'dridcard':"12345617890123",
            #         'draddress':"aaa",
            #         'dremail':"tes2tt@example.com"}
            # )
            # user0,xxx=User.objects.get_or_create(
            #     username="test22t",
            #     defaults={'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
            # )
            # user0.save()
            # userp0,xxx=UserProfile.objects.get_or_create(
                
            #     user=user0,
            #     defaults={'firstname':"Doctor",'lastname':"Tneitap",'role':1,'status':True}
            # )
            userp0=UserProfile.objects.get(
                firstname="Doctor",
                # defaults={'firstname':"Doctor",'lastname':"Tneitap",'role':1,'status':True}
            )
            # userp0.save()
            d1,xxx=Doctor.objects.get_or_create(
                userprofile=userp0,
                defaults={'department' : 'Cancer'}
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
            user1,xxx=User.objects.get_or_create(
                username="test21t",
                defaults={'password':make_password(password="1234",hasher='sha1'),'email':"mai12llll@mail.com"}
            )
            user1.save()
            userp1,xxx=UserProfile.objects.get_or_create(
                user=user1,
                defaults={'user':user1,'firstname':"QQQ",'lastname':"WWWW",'role':1,'status':True}
            )
            userp1.save()
            d2,xxx=Doctor.objects.get_or_create(
                userprofile=userp1,
                defaults={'department' : 'Cancer'}
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
                u = User(
                    username='username'+str(random.randrange(1,100000000)),
                    email='username'+str(random.randrange(1,100000000))+'@example.com',
                    password='pass'+str(random.randrange(1,100000000)),
                )
                u.save()
                up = UserProfile(
                        user=u,
                        firstname='name'+str(random.randrange(1,100)),
                        lastname='sur'+str(random.randrange(1,100)),
                        role=0,
                )
                up.save()
                pt = Patient(
                userprofile=up,
                sex=random.choice(['M','F']),
                birthdate=datetime.now()-timedelta(days=random.randrange(1000,10000)),
                idcard=str(random.randrange(1,100)),
                address=str(random.randrange(1,100)),
                phone=str(random.randrange(1,100)),

                )
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

                PatientVisitInfo.objects.filter(appointment=a).update(lastUpdate=v.lastUpdate-timedelta(hours=random.randrange(0,4)*random.randrange(0,5)*random.randrange(0,6)*random.randrange(0,7)))

            return render(request, 'seed.html')
        #else :
            #return HttpResponseRedirect('/default/')
    #else :
        #return HttpResponseRedirect('/default/')