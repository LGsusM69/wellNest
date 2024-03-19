from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import createview
from .forms import JournalEntryForm
from datetime import date

from .models import Journal, DailyCheckIn, Plans, DailySummary

# Create your views here.

class JournalCreate(CreateView):
    model = Journal
    fields = '__all__'


def home(request):
    if request.method == 'POST':
        mood_form = MoodCheckForm(request.POST)
    return render(request, 'home.html')

def checkins(request):
    return render(request, 'features/checkins.html')

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
        print("squidward")
        print(form)
        if form.is_valid():
            print("it is valid")
            form.save()
            return redirect('journal_list')
        else:
            print("not valid")
            form = JournalEntryForm()
        return render(request, 'features/journal.html', {'from': form,})
        
