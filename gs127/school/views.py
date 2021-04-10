from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import Student
from django.views.generic.base import TemplateView

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password'] 
    success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'
    