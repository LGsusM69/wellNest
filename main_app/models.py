from django.db import models
from django.contrib.auth.models import User 
import datetime
## Add 'user = models.ForeignKey(User, on_delete=models.CASCADE)' to dailysummaries model ##

# Create your models here.

    
class Journal(models.Model):
    dailyPrompt = models.TextField(max_length=250)
    freeWrite = models.TextField(max_length=1000)
    date = models.DateField(default=datetime.date.today)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    
class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    #list of available moods
    sleep = models.CharField(max_length=100)
    #int 0 - 100
    diet = models.CharField(max_length=100)
    #list of options
    exercise = models.CharField(max_length=100)
    dailyPractices = models.CharField(max_length=100)
    date = models.DateField()

class Plan(models.Model):
    plan = models.CharField(max_length=100)
    date = models.DateField(default=datetime.date.today)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DailySummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(datetime.date.today)
    mood_check = models.CharField(max_length=100)
    sleep_check = models.CharField(max_length=100)
    eating_check = models.CharField(max_length=100)
    exercise_check = models.CharField(max_length=100)
    journal_entry = models.TextField()

    def __str__(self):
        return f'Daily Summary for {self.date}'