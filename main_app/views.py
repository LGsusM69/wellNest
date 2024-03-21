from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import JournalEntryForm, PhotoUploadForm
from datetime import date
from random import randint

from .models import Journal, DailyCheckIn, Plan, DailySummary, DailyPrompt

# Create your views here.

class CheckinCreate(CreateView):
    model = DailyCheckIn
    fields = ["mood", "sleep", "diet", "exerciseType", 
              "duration", "intensity", "practices",
                "improvements"
              
              ]
    success_url = '/checkins'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

class JournalCreate(CreateView):
    model = Journal
    fields = ["freeWrite"]
    success_url = '/journal'

    def form_valid(self, form):
    # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        count = DailyPrompt.objects.count()
        #daily_prompt = DailyPrompt.objects.first()
        daily_prompt = DailyPrompt.objects.all()[randint(0, count -1)]
        context['daily_prompt'] = daily_prompt
        return context
    
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
    if request.method == 'POST':
        journal_form = JournalEntryForm(request.POST)
        photo_form = PhotoUploadForm(request.POST, request.FILES)
        if journal_form.is_valid():
            # Process journal entry form
            journal_entry = journal_form.save(commit=False)
            journal_entry.user = request.user
            journal_entry.save()
            return redirect('journal')  # Redirect to the journal page after form submission
        elif photo_form.is_valid():
            # Process photo upload form
            photo = photo_form.save(commit=False)
            photo.user = request.user
            photo.save()
            return redirect('journal')  # Redirect to the journal page after form submission
    else:
        journal_form = JournalEntryForm()
        photo_form = PhotoUploadForm()

    return render(request, 'features/journal.html', {'journal_form': journal_form, 'photo_form': photo_form, 'current_date': current_date })



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

from django.shortcuts import render, redirect
from .forms import PhotoUploadForm


def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user  # will assign the logged-in user to the photo/
            photo.save()
            return redirect('journal')  # Redirect to the journal page after upload
    else:
        form = PhotoUploadForm()
    return render(request, 'journal.html', {'form': form})


