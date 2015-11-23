from django import forms
from django.contrib.auth.models import User
from Authentication.models import UserProfile,Patient


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input-lg','placeholder':'Password'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Username'}),
            'email': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Email'}),
        }

        

class UserProfileForm(forms.ModelForm):
    
    class Meta:
        model = UserProfile
        fields = ('firstname','lastname')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Lastname'}),
        }

class PatientProfile(forms.ModelForm):
    CHOICES = (('M','Male'),('F','Female'))
    sex =  forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES, error_messages={'required':"Please select sex"})

    class Meta:
        model = Patient
        fields = ('sex','birthdate','idcard','phone','address')
        widgets = {
            'birthdate': forms.DateInput(attrs={'class': 'form-control input-lg input-datepicker','placeholder':'Birthdate','data-date-format':'mm/dd/yy'}),
            'idcard': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'ID card'}),
            'phone': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Phone'}),
            'address': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Address'}),
        }

class AdminCreateUser(forms.ModelForm):
    CHOICES = (('1','Doctor'),('2','Nurse'),('3','Officer'),('4','Pharmacist'),('5','Admin'))
    role = forms.ChoiceField(widget=forms.RadioSelect(attrs={'class':'radio-inline'}), choices=CHOICES, error_messages={'required':"Please select role"})

    class Meta:
        model = UserProfile
        fields = ('firstname','lastname','role')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Lastname'}),
        }

class AdminCreateDoctor(forms.ModelForm):
    Department = forms.ModelChoiceField(queryset=dee,to_field_name="name")
    class Meta:
        model = Doctor
        fields = ('department')
