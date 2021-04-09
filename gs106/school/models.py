from django.db import models
from .managers import CustomManager

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()

    students = CustomManager()
    objects = CustomManager()
    