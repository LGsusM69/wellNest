from django.db import models

from django.contrib.auth.models import User
## Add 'user = models.ForeignKey(User, on_delete=models.CASCADE)' to dailysummaries model ##

# Create your models here.

    
class Journal(models.Model):
    dailyPrompt = models.TextField(max_length=250)
    freeWrite = models.TextField(max_length=1000)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

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

class Plans(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    plans = models.CharField(max_length=100)

##class DailySummaries():
    ##user = models.ForeignKey(User, on_delete=models.CASCADE)
    ##date = models.DateField()
    #date = check-in ref
    #journalEntry = journal reference