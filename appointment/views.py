from django.shortcuts import render
from django.http import HttpResponse

from .forms import AppForm

import json
from django.http import JsonResponse
from .models import Department,Dee

#for restframework
from rest_framework import viewsets
from .serializers import DepartmentSerializer, DeeSerializer

#for restframework
class DepartmentViewset(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class DeeViewset(viewsets.ModelViewSet):
    queryset = Dee.objects.all()
    serializer_class = DeeSerializer

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def doctor(request):
    return HttpResponse(json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}]))

def show(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AppForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...

            data = {'form': form.cleaned_data , 'hello': 'world'}
            return HttpResponse(json.dumps(data), content_type='application/json')

            # redirect to a new URL:
            #return HttpResponseRedirect('/app/')
			
            

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AppForm()
        department = Department.objects.all()

    return render(request, 'default/appointment.html', {'department': department,'form':form})


