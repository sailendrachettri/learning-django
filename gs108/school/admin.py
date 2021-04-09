from django.contrib import admin
from .models import Student, ProxyStudent

@admin.register(Student)
class ModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']

@admin.register(ProxyStudent)
class ProxyStudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll']