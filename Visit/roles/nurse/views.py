from datetime import datetime,timedelta
from appointment.models import Appointment
from Visit.models import PatientVisitInfo
from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from Authentication.models import UserProfile
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from Authentication.models  import Patient

# Create your views here.
# please remove comment syntax to use authen
def index(request):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==2:
			return render(request, 'nurse/index.html')
		#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')
def view(request):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==2:
			return render(request, 'nurse/view.html',{'table':PatientVisitInfo.objects.filter(
		 		lastUpdate__day=datetime.now().day,
		 		lastUpdate__month=datetime.now().month,
		 		lastUpdate__year=datetime.now().year,
		 		status=0
			)})
	#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')
def edit(request,num):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==2:
			return render(request, 'nurse/edit.html', {'num':num})
	#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')

#Method for get user profile
def getUserProfile(user):
    return UserProfile.objects.get(user=user)