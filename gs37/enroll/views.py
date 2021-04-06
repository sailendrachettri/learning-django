from django.shortcuts import render
from .forms import StudentResgistration

def showformdata(request):

    if request.method == 'POST':
        fm = StudentResgistration(request.POST)
        if fm.is_valid():
            name = request.POST['name'] #bad practice
            email = fm.cleaned_data['email'] # good pracitce
            pw = fm.cleaned_data['password'] # good pracitce
            print('form validated', name, email, pw)
    else:
        fm = StudentResgistration()
        # print('GET Request is this!')

    return render(request, 'enroll/userregistration.html', {'form': fm})