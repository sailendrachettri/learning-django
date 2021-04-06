from django import forms
from django.core import validators


class StudentResgistration(forms.Form):
    name = forms.CharField(error_messages={'required':'Enter Your Name: '})
    email = forms.EmailField(error_messages={'required':'Enter Your Email: '})
    password = forms.CharField(widget=forms.PasswordInput, error_messages={'required':'Enter Your Password'})
    



 