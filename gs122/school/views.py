from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView

class StudentDetailView(DetailView):
    model = Student