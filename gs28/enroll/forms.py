from django import forms

class StudentResgistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()