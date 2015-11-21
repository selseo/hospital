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
        fields = ('firstname','lastname','sex','idcard','phone')
        widgets = {
            'firstname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Firstname'}),
            'lastname': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Lastname'}),
            'sex': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Sex'}),
            'idcard': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'ID card'}),
            'phone': forms.TextInput(attrs={'class': 'form-control input-lg','placeholder':'Phone'}),
        }
