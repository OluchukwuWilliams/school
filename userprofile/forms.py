from django import forms 
from django.forms import ModelForm 
from userprofile.models import *
from django.contrib.auth.forms import UserCreationForm 


class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField()

    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile 
        fields = ['first_Name', 'last_Name', 'pix', 'email', 'address', 'phone', 'dob', 'nationality', 'gender']

        GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('others', 'others'),
        ]

        STATE = [
            ('Enugu', 'Enugu'),
            ('Delta', 'Delta'),
            ('Ekiti', 'Ekiti'),
            ('Ogun', 'Ogun'),
            ('Abia', 'Abia'),
            ('Lagos', 'Lagos'),
            ('Akwa-Ibom', 'Akwa-Ibom'),
            ('Imo', 'Imo'),
            ('Edo', 'Edo'),
        ]

        Widget = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'Last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'pix': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Profile Image'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Home Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'dob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}, choices= GENDER),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}, choices= STATE),
        }