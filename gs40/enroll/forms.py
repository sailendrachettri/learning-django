from django import forms

class StudentResgistration(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput) 

    def clean_name(self):
        valName = self.cleaned_data['name']
        if len(valName) < 4:
            raise forms.ValidationError("Enter more than or equal 4 characters!")
        return valName
