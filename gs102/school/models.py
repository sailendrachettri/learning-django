from django.db import models

class CommonInfo(models.Model):
    name = models.CharField(max_length=90)
    age = models.IntegerField() 
    date = models.DateField()
    class Meta:
        abstract = True   

class Student(CommonInfo):
    fees = models.IntegerField()
    date = None # Overriding CommonInfo


class Teacher(CommonInfo):
    salary = models.IntegerField()


class Contractor(CommonInfo):
    date = models.DateTimeField() # Overriding CommonInfo
    payment = models.IntegerField()

    