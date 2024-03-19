from django.contrib import admin

from .models import DailyCheckIn, Journal, User, DailySummary, Plan

# Register your models here.

admin.site.register(DailyCheckIn)
admin.site.register(Journal)
admin.site.register(DailySummary)
admin.site.register(Plan)
