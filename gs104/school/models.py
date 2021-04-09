from django.db import models

class ExamCenter(models.Model):
    cname = models.CharField(max_length=90)
    city = models.CharField(max_length=90)

class MyExamCenter(ExamCenter):
    class Meta:
        proxy = True
        ordering = ['city']