from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic import createview
from .forms import JournalEntryForm
from datetime import date

from .models import Journal, DailyCheckIn, Plans

# Create your views here.

class JournalCreate(CreateView):
    model = Journal
    fields = '__all__'


def home(request):
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
    return render(request, 'features/dailysummaries.html')

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
        
