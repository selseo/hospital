from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'doctor_timetable/index.html'

    def get_queryset(self):
    	return '';