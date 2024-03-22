from django.db import models
from django.contrib.auth.models import User 
import datetime
## Add 'user = models.ForeignKey(User, on_delete=models.CASCADE)' to dailysummaries model ##

# Create your models here.

    
class Journal(models.Model):
    freeWrite = models.TextField(max_length=1000)
    date = models.DateField(default=datetime.date.today)
    photo = models.ImageField(upload_to='journal_photos/', blank=True, null=True)  # New field for photos by murs


    user = models.ForeignKey(User, on_delete=models.CASCADE)

class DailyPrompt(models.Model):
    prompt = models.CharField(max_length=100)

    
class DailyCheckIn(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mood = models.CharField(max_length=100)
    #list of available moods
    sleep = models.CharField(max_length=100)
    #int 0 - 100
    diet = models.TextField(max_length=500)
    #list of options

    exerciseType = models.CharField(max_length=100)
    duration = models.IntegerField(default=1)
    intensity = models.CharField(max_length=100)
    practices = models.CharField(max_length=100)
    improvements = models.TextField()



    date = models.DateField(default=datetime.date.today)


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

    
class Photo(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True)

    def __str__(self):
        return self.description  # customize this as needed.....


