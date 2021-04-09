from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    page_name = models.CharField(max_length=90)
    page_cat = models.CharField(max_length=90)
    page_publish_date = models.DateField()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=90)
    post_cat = models.CharField(max_length=90)
    post_publish_date = models.DateField() 

class Song(models.Model):
    user = models.ManyToManyField(User)
    user = models.CharField(max_length=90)
    song_name = models.CharField(max_length=90)
    song_duration = models.IntegerField() 

    def written(self):
        return ', '.join([str(p) for p in self.user.all()]) 


