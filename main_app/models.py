from django.db import models

from django.contrib.auth.models import User
## Add 'user = models.ForeignKey(User, on_delete=models.CASCADE)' to dailysummaries model ##

# Create your models here.


class User(models.Model):
    userName = models.CharField(max_length=100)
    passWord = models.CharField()
    email = models.CharField()

    
class Journal(models.Model):
    dailyPrompt = models.TextField(max_length=250)
    freeWritte = models.TextField(max_length=1000)

class DailyCheckIn(models.Model):
    mood = models.CharField()
    sleep = models.CharField()
    diet = models.CharField()
    exercise = models.CharField()
    dailyPractices = models.CharField()