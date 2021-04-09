from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    roll = models.IntegerField()
    # objects = models.Manager() # Bydefault
    students = models.Manager()
    