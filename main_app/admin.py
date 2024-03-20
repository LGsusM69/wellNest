from django.contrib import admin

from .models import DailyCheckIn, Journal, User, DailySummary, Plan, DailyPrompt

# Register your models here.

admin.site.register(DailyCheckIn)
admin.site.register(DailySummary)
admin.site.register(Plan)
admin.site.register(DailyPrompt)
admin.site.register(Journal)