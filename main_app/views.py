from django.shortcuts import render, redirect
from .forms import JournalEntryForm
from datetime import date

# Create your views here.


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'features/dashboard.html')

def checkins(request):
    return render(request, 'features/checkins.html')

def journal(request):
    current_date = date.today()
    print('Today is', current_date)
    return render(request, 'features/journal.html', {'current_date': current_date})

def plans(request):
    return render(request, 'features/plans.html')

def dailysummaries(request):
    return render(request, 'features/dailysummaries.html')

def new_journal(request):
    if request.method == 'POST':
        form = JournalEntryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('journal_list')
        else:
            form = JournalEntryForm()
        return render(request, 'journal.html', {'from': form,})
        