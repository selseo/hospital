from datetime import datetime,timedelta
from appointment.models import Appointment
from Visit.models import *
from Medicine.models import Medicine
from Disease.models import Disease
from django.shortcuts import get_object_or_404, render, redirect
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
# Create your views here.
# please remove comment syntax to use authen
def index(request):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==1://Doctor
			return render(request, 'doctor/index.html')
		#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')

def view(request):
	#if request.user.is_authenticated():
		#if getUserProfile(request.user).role==1://Doctor
			return render(request, 'doctor/view.html',{'table':PatientVisitInfo.objects.filter(
		 		# lastUpdate__day=datetime.now().day,
		 		# lastUpdate__month=datetime.now().month,
		 		# lastUpdate__year=datetime.now().year,
		 		status=1
			)})
	#else :
			#return HttpResponseRedirect('/default/')
	#else :
		#return HttpResponseRedirect('/default/')
@csrf_exempt
def addDisease(request,num):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)

	if request.method == 'POST':
		ICD10 = request.POST["ICD10"]
		myDisease = get_object_or_404(Disease, ICD10=ICD10)
		if myDisease and myPatientVisitInfo:
			myPatientVisitInfo.diseases.add(myDisease)

	DiseaseAll = Disease.objects.filter(availability = 1)
	myDisease = myPatientVisitInfo.diseases.all()
	for Di in myDisease:
		DiseaseAll = DiseaseAll.exclude(ICD10=Di.ICD10)
	
	myPrescription = myPatientVisitInfo.prescription_set.all()
	MedicineAll = Medicine.objects.filter(availability = 1)
	myMedicine = myPatientVisitInfo.medicines.all()
	for Med in myMedicine:
		MedicineAll = MedicineAll.exclude(name=Med.name)

	return render(request,'doctor/edit.html',{'myPatientVisitInfo':myPatientVisitInfo, 'myPrescription':myPrescription,'Medicines': MedicineAll,'myMedicine' : myMedicine,'Diseases':DiseaseAll,'myDisease' : myDisease,'num' : num})

@csrf_exempt
def addMedicine(request,num):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)
	

	if request.method == 'POST':
		medicine_name = request.POST["medicine_name"]
		myMedicine1 = get_object_or_404(Medicine, name=medicine_name)
		if myMedicine1 and myPatientVisitInfo:
			myPatientVisitInfo.medicines.add(myMedicine1)

	myPrescription = myPatientVisitInfo.prescription_set.all()
	DiseaseAll = Disease.objects.filter(availability = 1)
	myDisease = myPatientVisitInfo.diseases.all()
	for Di in myDisease:
		DiseaseAll = DiseaseAll.exclude(ICD10=Di.ICD10)
	
	MedicineAll = Medicine.objects.filter(availability = 1)
	myMedicine = myPatientVisitInfo.medicines.all()
	for Med in myMedicine:
		MedicineAll = MedicineAll.exclude(name=Med.name)

	return render(request,'doctor/edit.html',{'myPatientVisitInfo':myPatientVisitInfo, 'myPrescription':myPrescription,'Medicines': MedicineAll,'myMedicine' : myMedicine,'Diseases':DiseaseAll,'myDisease' : myDisease,'num' : num})


@csrf_exempt
def deleteDisease(request,num,ICD10):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)
	myDisease = get_object_or_404(Disease, ICD10=ICD10)

	if myDisease and myPatientVisitInfo:
			myPatientVisitInfo.diseases.remove(myDisease)

	myPrescription = myPatientVisitInfo.prescription_set.all()

	DiseaseAll = Disease.objects.filter(availability = 1)
	myDisease = myPatientVisitInfo.diseases.all()
	for Di in myDisease:
		DiseaseAll = DiseaseAll.exclude(ICD10=Di.ICD10)
	
	MedicineAll = Medicine.objects.filter(availability = 1)
	myMedicine = myPatientVisitInfo.medicines.all()
	for Med in myMedicine:
		MedicineAll = MedicineAll.exclude(name=Med.name)
		
	return render(request,'doctor/edit.html',{'myPatientVisitInfo':myPatientVisitInfo, 'myPrescription':myPrescription,'Medicines': MedicineAll,'myMedicine' : myMedicine,'Diseases':DiseaseAll,'myDisease' : myDisease,'num' : num})

@csrf_exempt
def deleteMedicine(request,num,medicine_name):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)
	myMedicine1 = get_object_or_404(Medicine, name=medicine_name)

	if myMedicine1 and myPatientVisitInfo:
			myPatientVisitInfo.medicines.remove(myMedicine1)

	myPrescription = myPatientVisitInfo.prescription_set.all()

	DiseaseAll = Disease.objects.filter(availability = 1)
	myDisease = myPatientVisitInfo.diseases.all()
	for Di in myDisease:
		DiseaseAll = DiseaseAll.exclude(ICD10=Di.ICD10)
	
	MedicineAll = Medicine.objects.filter(availability = 1)
	myMedicine = myPatientVisitInfo.medicines.all()
	for Med in myMedicine:
		MedicineAll = MedicineAll.exclude(name=Med.name)

	return render(request,'doctor/edit.html',{'myPatientVisitInfo':myPatientVisitInfo, 'myPrescription':myPrescription,'Medicines':MedicineAll,'myMedicine' : myMedicine,'Diseases':DiseaseAll,'myDisease' : myDisease,'num' : num})


# @csrf_exempt
# def addMedicine(request,num):
# 	mymodel = get_object_or_404(PatientVisitInfo, appointment_id=num)
# 	form = PatientVisitDoctorForms(request.POST or None, instance=mymodel)
# 	if request.method == 'POST' and form.is_valid():
# 		mymodel = form.save(commit=False)
# 		# mymodel.status = 2
# 		mymodel.save()
# 		form.save_m2m()
# 		# prescription =  Prescription(patientVisitInfo =mymodel,medicines=form.cleaned_data['medicines']  )
# 		return redirect('doctor/edit.html', { 'form' : form , 'num' : num})
# 	return render(request, 'doctor/edit.html', { 'form' : form , 'num' : num})

@csrf_exempt
def editStatus1(request,num):
	myPatientVisitInfo = get_object_or_404(PatientVisitInfo, appointment_id=num)
	myPrescription = myPatientVisitInfo.prescription_set.all()
	if request.method == 'POST':
		myPatientVisitInfo.status = 2
		myPatientVisitInfo.note = request.POST["note"]
		myMedicine = myPatientVisitInfo.medicines.all()
		for prescription in myPrescription:
			name = str(prescription.medicines) + "_amount"
			prescription.amount = request.POST[name]
			name = str(prescription.medicines) + "_usage"
			prescription.usage = request.POST[name]
			prescription.save()
		myPatientVisitInfo.save()
		return redirect('/visit/doctor/view')

	myPrescription = myPatientVisitInfo.prescription_set.all()

	DiseaseAll = Disease.objects.filter(availability = 1)
	myDisease = myPatientVisitInfo.diseases.all()
	for Di in myDisease:
		DiseaseAll = DiseaseAll.exclude(ICD10=Di.ICD10)
	
	MedicineAll = Medicine.objects.filter(availability = 1)
	myMedicine = myPatientVisitInfo.medicines.all()
	for Med in myMedicine:
		MedicineAll = MedicineAll.exclude(name=Med.name)

	return render(request,'doctor/edit.html',{'myPatientVisitInfo':myPatientVisitInfo, 'myPrescription':myPrescription,'Medicines':MedicineAll,'myMedicine' : myMedicine,'Diseases':DiseaseAll,'myDisease' : myDisease,'num' : num})

#Method for get user profile
def getUserProfile(user):
    return UserProfile.objects.get(user=user)
