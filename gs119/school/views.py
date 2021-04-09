from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Student

class StudentListView(ListView):
    model = Student
    # template_name_suffix = '_list' #Default    
    # template_name_suffix = '_custom' #Custom template suffix name    
    # ordering = ['name']

    template_name = 'school/student.html'
    context_object_name = 'students'
