from django.shortcuts import render
from .forms import StudentResgistration
from django.http import HttpResponseRedirect
    
def showformdata(request):
    if request.method == 'POST':
        fm = StudentResgistration(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name'] 
            email = fm.cleaned_data['email'] 

            print("name: ", name)
            print("email: ", email)
    else:
        fm = StudentResgistration()
        # print('GET Request is this!')

    return render(request, 'enroll/userregistration.html', {'form': fm})