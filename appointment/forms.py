from django import forms
from django.forms.extras.widgets import SelectDateWidget
from .models import Department
from .models import Doctor
from .models import Dee

dee = Dee.objects.all()
department = Department.objects.all()
doctor = Doctor.objects.all()
BIRTH_YEAR_CHOICES = ('1980', '1981', '1982')
FAVORITE_COLORS_CHOICES = (
    ('1', 'Morning'),
    ('2', 'Afternoon'),
)

class AppForm(forms.Form):
	Department = forms.ModelChoiceField(queryset=dee,to_field_name="name")
	
	Doctor = forms.ModelChoiceField(queryset=doctor,to_field_name="drname")
	#Doctor = forms.CharField(required=True,max_length=100)
	Date = forms.DateField(widget=SelectDateWidget())
	Time = forms.MultipleChoiceField(required=True,
		widget=forms.CheckboxSelectMultiple, 
		choices=FAVORITE_COLORS_CHOICES)
	Symptom = forms.CharField(widget=forms.Textarea)
	Cause = forms.CharField(widget=forms.Textarea)

	Doctor.widget.attrs['class'] = 'form-control'
	Date.widget.attrs['class'] = 'form-control'
	Symptom.widget.attrs['class'] = 'form-control'
	Cause.widget.attrs['class'] = 'form-control'

class AppByStaff(forms.Form):
	patientid = forms.CharField(max_length=100, required=True, 
		widget=forms.TextInput(attrs={'placeholder': 'Patient ID', 'id': 'patientid', 'class': 'form-control'}))
	patientidcard = forms.CharField(label='Patient ID Card', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Citizen ID', 'id': 'patientidcard', 'class': 'form-control'}))
	patientname = forms.CharField(label='Your name', max_length=100,
		widget=forms.TextInput(attrs={'placeholder': 'Patient Name', 'id': 'patientname', 'class': 'form-control', 'disabled' : 'disabled'}))
	department = forms.ModelChoiceField(queryset=department, to_field_name="name", required=True, empty_label="--- Select Department ---",
		widget=forms.Select(attrs={'id': 'department', 'class': 'form-control'}))
	doctor = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'doctor', 'class': 'form-control'}))
	appointment = forms.ChoiceField(required=True,
		widget=forms.Select(attrs={'id': 'appointment', 'class': 'form-control'}))
	symptom = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'symptom', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your symptoms here ....'}))
	cause = forms.CharField(widget=forms.Textarea(
		attrs={'id': 'cause', 'class': 'form-control', 'rows': 4, 'placeholder' : 'Describe your causes here ....'}))
