from django.contrib import admin
from .models import ExamCenter, Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city', 'name', 'roll']

@admin.register(ExamCenter)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'cname', 'city']