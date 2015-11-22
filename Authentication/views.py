from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from .models import UserProfile
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
from django.shortcuts import render
from django.contrib.auth import authenticate, login,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from Authentication.forms import UserForm, UserProfileForm, PatientProfile,AdminCreateUser

from datetime import datetime
from django.utils import formats
from django.contrib.auth.models import User
# Create your views here.


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
            return render(request, 'admin/index_.html',{'total':count_user,'role':role})

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
            profile.status=1

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
            profile.status=1

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

# def doctor_index(request):
#     #comment

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
            profile.status=1

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
