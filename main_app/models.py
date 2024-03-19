from django.db import models

from django.contrib.auth.models import User
## Add 'user = models.ForeignKey(User, on_delete=models.CASCADE)' to dailysummaries model ##

# Create your models here.

    
class Journal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dailyPrompt = models.TextField(max_length=250)
    freeWrite = models.TextField(max_length=1000)

class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    sleep = models.CharField(max_length=100)
    diet = models.CharField(max_length=100)
    exercise = models.CharField(max_length=100)
    dailyPractices = models.CharField(max_length=100)
    date = models.DateField()

class Plans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plans = models.CharField(max_length=100)

##class DailySummaries():
    ##user = models.ForeignKey(User, on_delete=models.CASCADE)
    ##date = models.DateField()
    #date = check-in ref
    #journalEntry = journal reference