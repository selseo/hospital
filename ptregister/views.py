from django.http import HttpResponseRedirect, HttpResponse
from django.http import Http404
from .models import Patient
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.views import generic
# Create your views here.
def nptregform(request):
    return render(request, 'default/register.html',)

def submit(request):
    npatient=Patient.objects.create(
        ptusername=request.POST['ptusername'],
        ptpassword=request.POST['ptpassword'],
        ptphone=request.POST['ptphone'],
        ptname=request.POST['ptname'],
        ptsurname=request.POST['ptsurname'],
        ptsex=request.POST['ptsex'],
        ptbirthdate=request.POST['ptbirthdate'],
        ptidcard=request.POST['ptidcard'],
        ptaddress=request.POST['ptaddress'],
        ptemail=request.POST['ptemail']
    )
    npatient.save()
    return render(request, 'default/register.html',)
