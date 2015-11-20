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