from django import forms

class StudentResgistration(forms.Form):
    name = forms.CharField(label='Your Name', label_suffix='  ', initial='Your name here', required=False, disabled=True, help_text="30 character only!")

