from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import PhotoUploadForm
from datetime import date
from random import randint
from .models import DailyCheckIn

from .models import Journal, DailyCheckIn, Plan, DailySummary, DailyPrompt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User  # Add this import statement


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

# class JournalCreate(CreateView):
#     model = Journal
#     fields = ["freeWrite"]
#     success_url = '/journal'

#     def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#         form.instance.user = self.request.user  # form.instance is the cat
#     # Let the CreateView do its job as usual
#         return super().form_valid(form)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         count = DailyPrompt.objects.count()
#         #daily_prompt = DailyPrompt.objects.first()
#         daily_prompt = DailyPrompt.objects.all()[randint(0, count -1)]
#         context['daily_prompt'] = daily_prompt
#         return context

from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Journal, DailyPrompt
from random import randint

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ["freeWrite"]
    success_url = '/journal'

    def form_valid(self, form):
        # Debug statement to check the type of self.request.user
        print(type(self.request.user))

        # Assign the logged-in user (self.request.user) if it's a valid User instance
        if isinstance(self.request.user, User):
            form.instance.user = self.request.user
        else:
            # Handle the case when self.request.user is not a valid User instance
            print("Error: Invalid user instance")

        # Let the CreateView do its job as usual
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        count = DailyPrompt.objects.count()
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


def checkin_create(request):
    if request.methd == "POST":
        form = {
            'mood': request.POST.get('mood'),
            'sleep': request.POST.get('sleep'),
            'diet': request.POST.get('diet'),
            'exerciseType': request.POST.get('exerciseType'),
            'duration': request.POST.get('duration'),
            'intensity': request.POST.get('intensity'),
            'practices': request.POST.get('practices'),
            'improvements': request.POST.get('improvements'),
        }
        if all(form.values()):
            DailyCheckin.objects.create(
                mood = form['mood'],
                sleep = form['sleep'],
                diet = form['diet'],
                exerciseType = form['exerciseType'],
                duration = form['duration'],
                intenstity = form['intensity'],
                practices = form['practices'],
                improvements = form['improvements'],
            )
            return redirect('checkins/')
        else:
            form = {}
        #return render(request, 'your_template.html', {'form': form})
        return redirect('checkins/')


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
