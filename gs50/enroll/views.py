from django.shortcuts import render
from .forms import StudentResgistration
from django.http import HttpResponseRedirect
    
def showformdata(request):
    if request.method == 'POST':
        fm = StudentResgistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name'] 
            em = fm.cleaned_data['email'] 
            pw = fm.cleaned_data['password']  

            print(nm)
            print(em)
            print(pw)

    else:
        fm = StudentResgistration()
        # print('GET Request is this!')

    return render(request, 'enroll/userregistration.html', {'form': fm})