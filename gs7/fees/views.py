from django.shortcuts import render
from django.http import HttpResponse

def learn_python(request):
    return HttpResponse("This is learn python from fees")

def learn_django(request):
    return HttpResponse("This is learn django from fees")