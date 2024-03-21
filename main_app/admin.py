from django.contrib import admin

# remove user vs
from .models import DailyCheckIn, Journal, DailySummary, Plan, DailyPrompt

# Register your models here.

admin.site.register(DailyCheckIn)
admin.site.register(Journal)
admin.site.register(DailySummary)
admin.site.register(Plan)
admin.site.register(DailyPrompt)
