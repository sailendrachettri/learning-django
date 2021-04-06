from django.shortcuts import render

# Create your views here.
def course(request):
    return render(request, 'course/courseone.html')

def home(request):
    return render(request, 'course/home.html')