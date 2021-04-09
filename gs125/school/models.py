from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=90)
    roll = models.IntegerField()
    course = models.CharField(max_length=90)