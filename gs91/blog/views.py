from django.shortcuts import render, HttpResponse

def home(request):
    print('I am View')
    return HttpResponse('Go to home')
