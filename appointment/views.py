from django.shortcuts import render
from django.http import HttpResponse

from .forms import AppForm

import json
from django.http import JsonResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

# def show(request):
#     return render(request, 'default/appointment.html')

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

    return render(request, 'default/appointment.html', {'form': form})