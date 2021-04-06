from django.shortcuts import render
from .forms import StudentResgistration
from django.http import HttpResponseRedirect
from .models import User
    
def showformdata(request):
    if request.method == 'POST':
        fm = StudentResgistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name'] 
            em = fm.cleaned_data['email'] 
            pw = fm.cleaned_data['password']  
            # reg = User(name=nm, password=pw, email=em)
            reg = User(id=1)
            # reg.delete()
            # reg = User(id=1, name=nm, password=pw, email=em) # edit because of ID
            reg.save()

    else:
        fm = StudentResgistration()
        # print('GET Request is this!')

    return render(request, 'enroll/userregistration.html', {'form': fm})