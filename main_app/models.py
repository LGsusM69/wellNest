from django.db import models

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