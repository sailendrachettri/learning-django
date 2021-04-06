from django.shortcuts import render
from .forms import StudentResgistration

def showformdata(request):
    fm = StudentResgistration()
    return render(request, 'enroll/userregistration.html', {'form': fm})