from django.shortcuts import render, HttpResponse
from django.template.response import TemplateResponse

def home(request):
    print('I am View')
    return HttpResponse('This is home')

def excp(request):
    print('I am EXCP View')
    a = 10/0
    return HttpResponse('This is Excp Page')

def user_info(request):
    print('I am User+info View')
    context = {'name': 'Rahul'}
    return TemplateResponse(request, 'blog/user.html', context)

