from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Disease
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.contrib.auth.decorators import login_required, user_passes_test
from Authentication.models import UserProfile
# Create your views here.
#Method for get user profile
def getUserProfile(user):
    return UserProfile.objects.get(user=user)
def admin_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==5):
        return True;
    return False;

@login_required
@user_passes_test(admin_check)
@csrf_exempt
def index(request):

	#if request.user.is_authenticated():
        #if getUserProfile(request.user).role==5:
			return render(request,'admin/disease.html',{'table':Disease.objects.all(),'length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})
		#else :
            #return HttpResponseRedirect('/default/')
    #else :
        #return HttpResponseRedirect('/default/')

@login_required
@user_passes_test(admin_check)	
@csrf_exempt
def addDisease(request):
    if request.method == 'POST':
    	name = request.POST["name"]
    	ICD10 = request.POST["ICD10"]
    	if name and ICD10:
    		SNOMED = request.POST["SNOMED"]
    		DRG = request.POST["DRG"]
    		disease = Disease.objects.create(name=name,ICD10=ICD10,SNOMED=SNOMED,DRG=DRG)
    		disease.save()
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Success!','length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})
    	else :
    		return render(request,'admin/disease.html',{'table':Disease.objects.all(),'message':'Add Disease Fail! Please recheck diseases name and ICD10','length':Disease.objects.count(),'avail':Disease.objects.filter(availability=True).count()})

@login_required
@user_passes_test(admin_check)
@csrf_exempt
def setAvailability(request):
	# return HttpResponse('')
	
	ICD10 = request.POST["ICD10"]
	availability = request.POST["availability"]
	if availability == "true":
		di = Disease.objects.get(ICD10=ICD10)
		di.availability = True
		di.save()
	else : 
		di = Disease.objects.get(ICD10=ICD10)
		di.availability = False
		di.save()

	# .update(availability=availability)
	# print (di.availability)
	# di.availability = availability
	# di.save()
	# di = Disease.objects.filter(ICD10=ICD10)
	# res = serializers.serialize('json',di)
	return HttpResponse('')		

@csrf_exempt
def seed(request):
		dis,xxx=Disease.objects.get_or_create(
            name="Cholera due to Vibrio cholerae 01, biovar cholerae",
            defaults={'ICD10':"A00.0"}
        )
		dis.save()
		dis2,xxx=Disease.objects.get_or_create(
			name="Paratyphoid fever A",
			defaults={'ICD10':"A01.1"}
		)
		dis2.save()
		dis3,xxx=Disease.objects.get_or_create(
		name="Paratyphoid fever B",
		defaults={'ICD10':"A01.2"}
		)
		dis3.save()
		dis4,xxx=Disease.objects.get_or_create(
		name="Paratyphoid fever C",
		defaults={'ICD10':"A01.3"}
		)
		dis4.save()
		dis5,xxx=Disease.objects.get_or_create(
		name="Urban rabies",
		defaults={'ICD10':"A82.1"}
		)
		dis5.save()
		dis6,xxx=Disease.objects.get_or_create(
		name="Rabies, unspecified",
		defaults={'ICD10':"A82.9"}
		)
		dis6.save()
		dis7,xxx=Disease.objects.get_or_create(
		name="Superficial injury of nose",
		defaults={'ICD10':"S00.3"}
		)
		dis7.save()
		dis8,xxx=Disease.objects.get_or_create(
		name="Open wound of ear",
		defaults={'ICD10':"S01.3"}
		)
		dis8.save()
		dis9,xxx=Disease.objects.get_or_create(
		name="Burn of first degree of head and neck",
		defaults={'ICD10':"T20.1"}
		)
		dis9.save()
		dis10,xxx=Disease.objects.get_or_create(
		name="Burn of first degree of trunk",
		defaults={'ICD10':"T21.1"}
		)
		dis10.save()
		dis11,xxx=Disease.objects.get_or_create(
		name="Acute renal failure with tubular necrosis",
		defaults={'ICD10':"N17.0"}
		)
		dis11.save()
		return render(request, 'admin/seed.html')

