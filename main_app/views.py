from django.shortcuts import render, redirect
from .forms import JournalEntryForm
from datetime import date

from .models import Journal, DailyCheckIn, Plans, DailySummary

# Create your views here.


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'features/dashboard.html')

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


def new_journal(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
        else:
            form = JournalEntryForm()
        return render(request, 'journal.html', {'from': form,})
        
