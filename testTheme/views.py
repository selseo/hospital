from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'theme/doctor/index.html',)

def login(request):
	return render(request, 'theme/login.html',)


