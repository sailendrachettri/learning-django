from django.db import models

class Student(models.Model):
    stuid = models.IntegerField()
    stuname = models.CharField(max_length=30)
    stuemail = models.EmailField(max_length=40)
    stupass = models.CharField(max_length=30)
