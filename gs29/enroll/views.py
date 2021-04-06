from django.shortcuts import render
from .forms import StudentResgistration

def showformdata(request):
    # fm = StudentResgistration(auto_id=True)
    # fm = StudentResgistration(label_suffix=' - ')
    fm = StudentResgistration(initial={'name':'Sonam', 'email': 'example@mail.com'})
    return render(request, 'enroll/userregistration.html', {'form': fm})