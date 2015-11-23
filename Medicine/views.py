from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse,HttpRequest
from .models import Medicine
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
# Create your views here.
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
	return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})

@login_required
@user_passes_test(admin_check)
@csrf_exempt
def addMedicine(request):
    if request.method == 'POST':
    	name = request.POST["name"]
    	table = Medicine.objects.filter(name=name)
    	if name and (table.count()==0):
    		med = Medicine.objects.create(name=name)
    		med.save()
    		return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'message':"Add Medicine Success!",'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})
    	else:
    		return render(request,'admin/medicine.html',{'table':Medicine.objects.all(),'message':"Add Medicine Fail! Please recheck your medicine's name.",'length':Medicine.objects.count(),'avail':Medicine.objects.filter(availability=True).count()})

@login_required
@user_passes_test(admin_check)
@csrf_exempt
def setAvailability(request):
	name = request.POST["name"]
	availability = request.POST["availability"]
	if availability == "true":
		med = Medicine.objects.get(name=name)
		med.availability = True
		med.save()
	else : 
		med = Medicine.objects.get(name=name)
		med.availability = False
		med.save()
	return HttpResponse('')

@login_required
@user_passes_test(admin_check)
@csrf_exempt
def seed(request):
	# var drugs = ["Aspirin","Stomachic Mixture","Sulfacetamide Eye Drop","Liquid Paraffin Emulsion","Tetracycline Eye Ointment"
	# ,"Milk of Magnesia or Cream of Magnesia","Iodine Tincture","Senna (tablet)","Thimerosal Tincture","Oral Rehydration Salts","Analgesic Balm","Alumina and Magnesia (Tablet)","Toothache Drop","Alumina and Magnesia Oral Suspension","Burns and Scalds Mixture","Sodamint (tablet)","Salicylic Acid and sulphur ointment","Compound Cardamom Mixture","Salicylic Acid and sulphur Cream","Ammonium Carbonate and Glycyrrhiza Mixture","Magnesium Sulfate","Brown Mixture","Camphorated Opium Tincture","Compound Ammonium Carbonate Syrup","Iodine Tincture","Chlorpheniramine Maleate (tablet)","Eucalyptus Oil","Compound Ferrous Sulfate (tablet)","Aromatic Castor Oil","Multivitamin (tablet)","Cough Syrup","Vitamin B Complex (tablet)","Sodium Bicarbonate Mixture (pediatric)","Vitamin C (tablet)","Fish Liver Oil Capsule","Mebendazole (tablet)","Multivitamin Capsule","Aspirin (tablet)","Merbromin Solution","Paracetamol 325 mg.(tablet)","Kaolin Mixture with Pectin","Paracetamol 500 mg.(tablet)","Salol and Menthol Mixture","Paracetamol Syrup (pediatric)","Sulfadiazine Suspension (pediatric)","Asafetida Tincture","Chloroquine Phosphate (tablet)","Sodium Chloride Enema","Quinine Sulfate (tablet)","Mandl’s Paint","Sulfadoxine and Pyrimethamine (tablet)","Gentian Violet Solution","Sulfadiazine (tablet)","Cold Inhalant","Ephedrine Nasal Drop","Aromatic Ammonia Spirit","Nitrofurazone Ear Drop","Scabicide Emulsion","Acriflavine Solution","Sulphur Ointment","Pepermint Spirit.","Calamine Lotion","Povidone-Iodine Solution 10%","Coal Tar Ointment","Isopropyl Alcohol 70%","Whitfield’s Ointment"];
	drug,xxx=Medicine.objects.get_or_create(
		name="Aspirin",
	)
	drug.save()
	drug2,xxx=Medicine.objects.get_or_create(
		name="Stomachic Mixture",
	)
	drug2.save()	
	drug3,xxx=Medicine.objects.get_or_create(
		name="Liquid Paraffin Emulsion",
	)
	drug3.save()	
	drug4,xxx=Medicine.objects.get_or_create(
		name="Tetracycline Eye Ointment",
	)
	drug4.save()	
	drug5,xxx=Medicine.objects.get_or_create(
		name="Milk of Magnesia or Cream of Magnesia",
	)
	drug5.save()	
	drug6,xxx=Medicine.objects.get_or_create(
		name="Iodine Tincture",
	)
	drug6.save()	
	drug7,xxx=Medicine.objects.get_or_create(
		name="Thimerosal Tincture",
	)
	drug7.save()	
	drug8,xxx=Medicine.objects.get_or_create(
		name="Oral Rehydration Salts",
	)
	drug8.save()	
	drug9,xxx=Medicine.objects.get_or_create(
		name="Analgesic Balm",
	)
	drug9.save()	
	drug10,xxx=Medicine.objects.get_or_create(
		name="Alumina and Magnesia (Tablet)",
	)
	drug10.save()		
	return render(request, 'admin/seed.html')