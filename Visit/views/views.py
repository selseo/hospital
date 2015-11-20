from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
	return render(request, 'nurse/index.html')

# def index(request):
#     return HttpResponse("Nurse Index")