from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView
from .models import Student
from django import forms
from .forms import StudentForm


class StudentCreateView(CreateView):
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanks/'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'school/student_form.html'
    success_url = '/thanksupdate/'


class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/create/'

class ThanksUpdateTemplateView(TemplateView):
    template_name = 'school/thanksupdate.html'

class ThanksTemplateView(TemplateView):
    template_name = 'school/thanks.html'
