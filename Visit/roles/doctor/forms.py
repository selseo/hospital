from django import forms
from Visit.models import PatientVisitInfo
from Disease.models import Disease
from Medicine.models import Medicine
from django.db import models
from django.db.models.query import QuerySet

class PatientVisitDoctorForms(forms.ModelForm):
    # diseases = forms.ModelMultipleChoiceField(queryset=Disease.objects.all(),label='Select disease')
    class Meta:
        model = PatientVisitInfo
        fields = ['diseases','medicines']
    def __init__(self, *args, **kwargs):
         super(PatientVisitDoctorForms, self).__init__(*args, **kwargs)
         self.fields['diseases'].widget = forms.widgets.CheckboxSelectMultiple()
         self.fields['diseases'].queryset = Disease.objects.all()
         self.fields['diseases'].label = 'Select Disease'
         self.fields['medicines'].widget = forms.widgets.CheckboxSelectMultiple()
         self.fields['medicines'].queryset = Medicine.objects.all()
         self.fields['medicines'].label = 'Select Medicine'

