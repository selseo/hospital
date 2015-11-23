from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from django.contrib.auth.models import User
from .models import UserProfile,Patient
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Authentication.forms import UserForm, UserProfileForm, PatientProfile,AdminCreateUser
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from datetime import datetime
from django.utils import formats
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from django.contrib.auth.decorators import user_passes_test

def admin_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==5):
        return True;
    return False;

def doctor_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==1):
        return True;
    return False;

def patient_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==0):
        return True;
    return False;

def officer_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==3):
        return True;
    return False;

def nurse_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==2):
        return True;
    return False;

def pharmacist_check(user):
    userProfile = getUserProfile(user)
    if(userProfile.role==4):
        return True;
    return False;

def index(request):
    #variable for already check patient today
    #already_check_p=20
    #variable for uncheck patient today
   # uncheck_p=30
    #variable for all patient today
   # all_p=already_check_p+uncheck_p


    if request.user.is_authenticated():
        role = getUserProfile(request.user).role
        if role==0:
            #return render(request, 'default/index.html')
            return render(request, 'default/index.html',{
                'firstname':getUserProfile(request.user).firstname,
                'lastname':getUserProfile(request.user).lastname,
                'role':getUserProfile(request.user).role}
                )
        if role==1:
            #return render(request, 'theme/doctor/index.html')
            return render(request, 'doctor/index.html',{
                'al_check_p':1,
                'uncheck_p':2,
                'all_p':3,
                'firstname':getUserProfile(request.user).firstname,
                'lastname':getUserProfile(request.user).lastname,
                'role':getUserProfile(request.user).role}
                )
        if role==2:
            return HttpResponseRedirect('/visit/nurse')
        if role==3:
            #return HttpResponse("You are Officer")
            return render(request, 'officer/index.html',{
                'firstname':getUserProfile(request.user).firstname,
                'lastname':getUserProfile(request.user).lastname,
                'role':getUserProfile(request.user).role}
                )
        if role==4:
            #return HttpResponse("You are Pharmacist")
            return render(request, 'pharmacist/index.html',{
                'firstname':getUserProfile(request.user).firstname,
                'lastname':getUserProfile(request.user).lastname,
                'role':getUserProfile(request.user).role}
                )
        if role==5:
            #return HttpResponseRedirect('/default/createuser')
            users = User.objects.all()
            count_user = users.count()
            return render(request, 'admin/index_.html',{'total':count_user,
                'firstname':getUserProfile(request.user).firstname,
                'lastname':getUserProfile(request.user).lastname,
                'role':role})

    # Render the response and send it back!
    return render(request, 'theme/login.html',{'message':'You have to login to view this Page.'})

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        patient_form=PatientProfile(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid() and patient_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.role=0
            profile.status=True

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            patient=patient_form.save(commit=False)
            patient.userprofile=profile
            patient.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return render(request,'theme/login.html', {'registered': registered} )

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        patient_form = PatientProfile()

    # Render the template depending on the context.
    return render(request,
            'theme/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'patient_form':patient_form,'registered': registered} )

def some_view(request):
    if not request.user.is_authenticated():
        return HttpResponse("You are logged in.")
    else:
        return HttpResponse("You are not logged in.")

@login_required
def restricted(request):
    if getUserProfile(request.user).role==1:
        return HttpResponse("You are Doctor")
    else :
        return HttpResponse("Since you're logged in, you can see this text!")

#Method for get user profile
def getUserProfile(user):
    return UserProfile.objects.get(user=user)

@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/default/login')

def user_login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/default/')

    else :

    # If the request is a HTTP POST, try to pull out the relevant information.
        if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
                # We use request.POST.get('<variable>') as opposed to request.POST['<variable>'],
                # because the request.POST.get('<variable>') returns None, if the value does not exist,
                # while the request.POST['<variable>'] will raise key error exception
            username = request.POST.get('username')
            password = request.POST.get('password')

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
            user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
            if user:
            # Is the account active? It could have been disabled.
                if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                    login(request, user)
                    return HttpResponseRedirect('/default/')
                else:
                # An inactive account was used - no logging in!
                    return HttpResponse("Your authen account is disabled.")
            else:
            # Bad login details were provided. So we can't log the user in.
                print ("Invalid login details: {0}, {1}".format(username, password))
                return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
        else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
            return render(request, 'theme/login.html', {})

@user_passes_test(admin_check)
def admin_create_user(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        admin_user_form = AdminCreateUser(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and admin_user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = admin_user_form.save(commit=False)
            profile.user = user
            profile.status=True

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()


            # Update our variable to tell the template registration was successful.
            registered = True
            return render(request,'theme/login.html', {'registered': registered} )

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, admin_user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        admin_user_form = AdminCreateUser()

    # Render the template depending on the context.
    role = getUserProfile(request.user).role

    return render(request,
            'admin/addUser.html',
            {'user_form': user_form, 'admin_user_form': admin_user_form,'registered': registered,'role':role} )


def view_user_list(request):
    user_list = UserProfile.objects.all()
    paginator = Paginator(user_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        userls = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        userls = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        userls = paginator.page(paginator.num_pages)

    return render(request,'admin/viewuserlistpage.html', {'userls': userls})
    #return render (request,'admin/viewuserlistpage.html')

@csrf_exempt
def seed(request):
    # var drugs = ["Aspirin","Stomachic Mixture","Sulfacetamide Eye Drop","Liquid Paraffin Emulsion","Tetracycline Eye Ointment"
    # ,"Milk of Magnesia or Cream of Magnesia","Iodine Tincture","Senna (tablet)","Thimerosal Tincture","Oral Rehydration Salts","Analgesic Balm","Alumina and Magnesia (Tablet)","Toothache Drop","Alumina and Magnesia Oral Suspension","Burns and Scalds Mixture","Sodamint (tablet)","Salicylic Acid and sulphur ointment","Compound Cardamom Mixture","Salicylic Acid and sulphur Cream","Ammonium Carbonate and Glycyrrhiza Mixture","Magnesium Sulfate","Brown Mixture","Camphorated Opium Tincture","Compound Ammonium Carbonate Syrup","Iodine Tincture","Chlorpheniramine Maleate (tablet)","Eucalyptus Oil","Compound Ferrous Sulfate (tablet)","Aromatic Castor Oil","Multivitamin (tablet)","Cough Syrup","Vitamin B Complex (tablet)","Sodium Bicarbonate Mixture (pediatric)","Vitamin C (tablet)","Fish Liver Oil Capsule","Mebendazole (tablet)","Multivitamin Capsule","Aspirin (tablet)","Merbromin Solution","Paracetamol 325 mg.(tablet)","Kaolin Mixture with Pectin","Paracetamol 500 mg.(tablet)","Salol and Menthol Mixture","Paracetamol Syrup (pediatric)","Sulfadiazine Suspension (pediatric)","Asafetida Tincture","Chloroquine Phosphate (tablet)","Sodium Chloride Enema","Quinine Sulfate (tablet)","Mandl’s Paint","Sulfadoxine and Pyrimethamine (tablet)","Gentian Violet Solution","Sulfadiazine (tablet)","Cold Inhalant","Ephedrine Nasal Drop","Aromatic Ammonia Spirit","Nitrofurazone Ear Drop","Scabicide Emulsion","Acriflavine Solution","Sulphur Ointment","Pepermint Spirit.","Calamine Lotion","Povidone-Iodine Solution 10%","Coal Tar Ointment","Isopropyl Alcohol 70%","Whitfield’s Ointment"];
    user0,xxx=User.objects.get_or_create(
        username="user0",
        defaults={'username':"user0",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user0.save()
    userp0,xxx=UserProfile.objects.get_or_create(
        firstname="Patient",
        defaults={'user':user0,'firstname':"Patient",'lastname':"Tneitap",'role':0,'status':True}
    )
    userp0.save()
    userpp,xxx=Patient.objects.get_or_create(
        idcard="1100644983267",
        defaults={'userprofile':userp0,'sex':"f",'idcard':"1100644983267",'phone':"0839826174",'address':"1",'birthdate':"1984-11-21"}
    )
    userpp.save()

    user1,xxx=User.objects.get_or_create(
        username="user1",
        defaults={'username':"user1",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user1.save()
    userp1,xxx=UserProfile.objects.get_or_create(
        firstname="Doctor",
        defaults={'user':user1,'firstname':"Doctor",'lastname':"Rotcod",'role':1,'status':True}
    )
    userp1.save()

    user2,xxx=User.objects.get_or_create(
        username="user2",
        defaults={'username':"user2",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user2.save()
    userp2,xxx=UserProfile.objects.get_or_create(
        firstname="Nurse",
        defaults={'user':user2,'firstname':"Nurse",'lastname':"Rotcod",'role':2,'status':True}
    )
    userp2.save()

    user3,xxx=User.objects.get_or_create(
        username="user3",
        defaults={'username':"user3",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user3.save()
    userp3,xxx=UserProfile.objects.get_or_create(
        firstname="Officer",
        defaults={'user':user3,'firstname':"Officer",'lastname':"Rotcod",'role':3,'status':True}
    )
    userp3.save()

    user4,xxx=User.objects.get_or_create(
        username="user4",
        defaults={'username':"user4",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user4.save()
    userp4,xxx=UserProfile.objects.get_or_create(
        firstname="Pharmacist",
        defaults={'user':user4,'firstname':"Pharmacist",'lastname':"Rotcod",'role':4,'status':True}
    )
    userp4.save()

    user5,xxx=User.objects.get_or_create(
        username="user5",
        defaults={'username':"user5",'password':make_password(password="1234",hasher='sha1'),'email':"maillll@mail.com"}
    )
    user5.save()
    userp5,xxx=UserProfile.objects.get_or_create(
        firstname="Admin",
        defaults={'user':user5,'firstname':"Admin",'lastname':"Rotcod",'role':5,'status':True}
    )
    userp5.save()


    return HttpResponse("Seeddddd")


def officer_createPatient(request):
    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        patient_form=PatientProfile(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid() and patient_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.role=0
            profile.status=True

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            patient=patient_form.save(commit=False)
            patient.userprofile=profile
            patient.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/default/',{'a':'a'})

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, profile_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()
        patient_form = PatientProfile()

    # Render the template depending on the context.
    return render(request,
            'officer/addPatient.html',
            {'user_form': user_form, 'profile_form': profile_form, 'patient_form':patient_form,'registered': registered} )


@user_passes_test(admin_check)
def viewuser(request, userl_slug):

    # Create a context dictionary which we can pass to the template rendering engine.
    user_info = {}

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # So the .get() method returns one model instance or raises an exception.
        userl = UserProfile.objects.get(slug=userl_slug)
        user_info['firstname'] = userl.firstname
        user_info['lastname'] = userl.lastname
        user_info['role'] = userl.lastname

    except UserProfile.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything - the template displays the "no category" message for us.
        return HttpResponseRedirect('/default/viewuserlist/')

    ####### PLEASE EDIT TO DIRECT TO VIEW USER ##########
    return HttpResponse(user_info['firstname'])


@user_passes_test(admin_check)
def edituser(request, userl_slug):
    ##### THIS METHOD MUST EDIT#####
    ## It looks like viewusermethod but you should to edit to make it can edit user profile in database ##
    user_info = {}
    try:
        userl = UserProfile.objects.get(slug=userl_slug)
        user_info['firstname'] = userl.firstname
        user_info['lastname'] = userl.lastname
        user_info['role'] = userl.role
        userAccount = userl.user

    except UserProfile.DoesNotExist:
        return HttpResponseRedirect('/default/viewuserlist/')

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        admin_user_form = AdminCreateUser(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() or admin_user_form.is_valid():
            # Save the user's form data to the database.
            #user = user_form.save()
            userprofile = get_object_or_404(UserProfile,slug=userl_slug)
            #user = user_form.save()
            userprofile.firstname = admin_user_form.firstname

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            userAccount.set_password(userAccount.password)
            userAccount.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            userl = admin_user_form.save(commit=False)
            userl.user = user
            userl.status=True

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            #if 'picture' in request.FILES:
            #    profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            userl.save()


            # Update our variable to tell the template registration was successful.
            registered = True
            return HttpResponseRedirect('/default/viewuserlist/')

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print (user_form.errors, admin_user_form.errors)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm(initial={'username': userAccount.username,'password':userAccount.password})
       
        admin_user_form = AdminCreateUser(initial={
            'firstname': user_info['firstname'],
            'lastname':user_info['lastname'],
            'role':user_info['role']})



    return render(request,
            'admin/editUser.html',
            {'user_form': user_form, 'admin_user_form': admin_user_form,'registered': registered,'userl':userl} )



@user_passes_test(admin_check)
def testtry(request):
    return HttpResponse('You are admin')
