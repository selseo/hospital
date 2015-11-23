from datetime import datetime,timedelta
from appointment.models import Appointment
from Visit.models import PatientVisitInfo,Prescription
from django.shortcuts import get_object_or_404, render, redirect
from .forms import PatientVisitPharmacistForms
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from Authentication.models import UserProfile
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from Authentication.models  import Patient
from django.contrib.auth.decorators import login_required, user_passes_test
from Authentication.models import UserProfile
# Create your views here.
#Method for get user profile
def getUserProfile(user):
    return UserProfile.objects.get(user=user)
def pharmacist_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==4):
        return True;
    return False;
# Create your views here.
# please remove comment syntax to use authen
@login_required
@user_passes_test(pharmacist_check)
def index(request):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==4://Pharmacist
			prescription_num = Prescription.objects.filter(patientVisitInfo__lastUpdate__day=datetime.now().day,patientVisitInfo__lastUpdate__month=datetime.now().month,
				patientVisitInfo__lastUpdate__year=datetime.now().year).count()
			prescription_checked = Prescription.objects.filter(patientVisitInfo__lastUpdate__day=datetime.now().day,
		 		patientVisitInfo__lastUpdate__month=datetime.now().month,
		 		patientVisitInfo__lastUpdate__year=datetime.now().year,
		 		patientVisitInfo__status=3
		 		).count()
			prescription_unchecked = prescription_num - prescription_checked
			return render(request, 'pharmacist/index.html',{'table':PatientVisitInfo.objects.filter(
		 		lastUpdate__day=datetime.now().day,
		 		lastUpdate__month=datetime.now().month,
		 		lastUpdate__year=datetime.now().year,
		 		status=2
			),'prescription_num':prescription_num,
			'prescription_checked':prescription_checked,
			'prescription_unchecked':prescription_unchecked})
		#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')

@login_required
@user_passes_test(pharmacist_check)
@csrf_exempt
def editStatus2(request,num):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)
	myPrescription = myPatientVisitInfo.prescription_set.all()
	if request.method == 'POST':
		myPatientVisitInfo.status = 3
		myPatientVisitInfo.save()
		return redirect('/visit/pharmacist')
	return render(request,'pharmacist/edit.html',{'myPrescription':myPrescription,'num' : num,'pvi':myPatientVisitInfo})

