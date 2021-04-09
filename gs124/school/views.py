from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'
    
class StudentListView(ListView):
    model = Student