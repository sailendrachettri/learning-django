from django.shortcuts import render
from django.http import HttpResponse


def learn_django(request):
    return HttpResponse("Hello Django")


def var(request):
    a = 'variable'
    return HttpResponse(a)


def strf(request):
    a = 'String f'
    return HttpResponse(f"This is {a}")


def add(request):
    a = 5
    b = 5
    c = a + b
    return HttpResponse(c)
