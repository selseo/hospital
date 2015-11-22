from django import forms
from Visit.models import PatientVisitInfo
from Disease.models import Disease
from django.db import models
from django.db.models.query import QuerySet

class PatientVisitDoctorForms(forms.ModelForm):
    # diseases = forms.ModelMultipleChoiceField(queryset=Disease.objects.all(),label='Select disease')
    class Meta:
        model = PatientVisitInfo
        fields = ['diseases']
    def __init__(self, *args, **kwargs):
         super(PatientVisitDoctorForms, self).__init__(*args, **kwargs)
         self.fields['diseases'].widget = forms.widgets.CheckboxSelectMultiple()
         self.fields['diseases'].queryset = Disease.objects.all()

