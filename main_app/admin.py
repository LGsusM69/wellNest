from django.contrib import admin

from .models import DailyCheckIn, Journal, User

# Register your models here.

admin.site.register(DailyCheckIn)
admin.site.register(Journal)