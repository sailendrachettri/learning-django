from django.db import models

class User(models.Model):
    student_name = models.CharField(max_length=100)
    teacher_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=30)