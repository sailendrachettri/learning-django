from django.shortcuts import render
from .forms import SignupForm
from django.contrib import messages

def sign_up(request):
    if request.method == 'POST':
        fm = SignupForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created Successfully!')
            fm.save()
    else:
        fm = SignupForm()
    return render(request, 'enroll/signup.html', {'form':fm})
