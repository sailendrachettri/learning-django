from django.shortcuts import render
from django.http import HttpResponse

def learn_django(request):
    return HttpResponse("Hello django")