from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    template_name_suffix = '_list'    
    ordering = ['name']
