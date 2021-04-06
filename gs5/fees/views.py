from django.shortcuts import render
from django.http import HttpResponse

def learn_python(request):
    return HttpResponse("Hello Python")