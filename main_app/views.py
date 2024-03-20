from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import JournalEntryForm
from datetime import date, timedelta

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
    template_name = 'your_template.html'
    fields = ['plan']  # Specify the fields to include in the form

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['hours'] = ["06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"]
        return context

def home(request):
    return render(request, 'home.html')

def checkins(request):
    current_date = date.today()
    return render(request, 'features/checkins.html', {'current_date': current_date})

def journal(request):
    current_date = date.today()
    print('Today is', current_date)
    return render(request, 'features/journal.html', {'current_date': current_date})

def plans(request):
    current_date = date.today()
    def add_days(value, days):
        return value + timedelta(days=days)
    return render(request, 'features/plans.html', {'current_date': current_date, 'add_days': add_days})



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
