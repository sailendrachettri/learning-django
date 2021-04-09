from django.shortcuts import render
from .models import Student
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class StudentDetailView(DetailView):
    model = Student
    template_name = 'school/student.html'
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['all_student'] = self.model.objects.all().order_by('id')
        return context


class StudentListView(ListView):
    model = Student