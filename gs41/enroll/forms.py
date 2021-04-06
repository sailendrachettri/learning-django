from django import forms

class StudentResgistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField() 

    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        valemail = self.cleaned_data['email']

        if len(valname) < 4:
            raise forms.ValidationError('Name should be more than 5')
        if len(valemail) < 10:
            raise forms.ValidationError('Email should be more than 10')
