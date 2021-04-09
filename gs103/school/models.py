from django.db import models

class ExamCenter(models.Model):
    cname = models.CharField(max_length=100)
    city = models.CharField(max_length=70)
    

class Student(ExamCenter):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
