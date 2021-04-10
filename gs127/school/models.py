from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=90)
    email = models.EmailField()
    password = models.CharField(max_length=90)