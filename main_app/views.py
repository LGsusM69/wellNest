from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import JournalEntryForm
from datetime import date

from .models import Journal, DailyCheckIn, Plan, DailySummary

# Create your views here.

class JournalCreate(CreateView):
    model = Journal
    fields = ["dailyPrompt", "freeWrite"]
    success_url = '/journal'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    
class PlanCreate(CreateView):
    model = Plan
    fields = ["plan"]
    success_url = '/plans'

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
        # Let the CreateView do its job as usual
        return super().form_valid(form)


def home(request):
    return render(request, 'home.html')

def checkins(request):
    current_date = date.today()
    print('Today is', current_date)
    return render(request, 'features/checkins.html', {'current_date': current_date})

def journal(request):
    current_date = date.today()
    print('Today is', current_date)
    return render(request, 'features/journal.html', {'current_date': current_date})

def plans(request):
    return render(request, 'features/plans.html')

def dailysummaries(request):
    daily_summaries = DailySummary.objects.all()
    daily_summaries_by_date = {}
    for daily_summary in daily_summaries:
        date_key = daily_summary.date.strftime('%B %d, %Y')
        if date_key in daily_summaries_by_date:
            daily_summaries_by_date[date_key].append(daily_summary)
        else:
            daily_summaries_by_date[date_key] = [daily_summary]

    context = {
        'daily_summaries_by_date': daily_summaries_by_date,
    }
    return render(request, 'features/dailysummaries.html', context)
