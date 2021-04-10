from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.base import TemplateView
from .models import Student

class StudentCreateView(CreateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanks/'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'

class StudentUpdateView(UpdateView):
    model = Student
    fields = ['name', 'email', 'password']
    success_url = '/thanksupdate/'


class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'
