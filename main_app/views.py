from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import PhotoUploadForm
from datetime import date
from random import randint
from .models import Journal, DailyCheckIn, Plan, DailySummary, DailyPrompt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User  
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from datetime import datetime



# Create your views here.

class CheckinCreate(LoginRequiredMixin, CreateView):
    model = DailyCheckIn
    fields = ["mood", "sleep", "diet", "exerciseType", 
              "duration", "intensity", "practices",
              "improvements"
              ]
    success_url = '/checkins'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ["freeWrite"]
    success_url = '/journal'

    def form_valid(self, form):
        print(type(self.request.user))

        if isinstance(self.request.user, User):
            form.instance.user = self.request.user
        else:
            print("Error: Invalid user instance")

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        count = DailyPrompt.objects.count()
        daily_prompt = DailyPrompt.objects.all()[randint(0, count -1)]
        context['daily_prompt'] = daily_prompt
        return context


    
# class PlanCreate(LoginRequiredMixin, CreateView):
#     model = Plan
#     fields = ["plan"]
#     success_url = '/plans'

#     def form_valid(self, form):
#         if isinstance(self.request.user, User):
#             form.instance.user = self.request.user
#         else:
#             print("Error: Invalid user instance")

#         return super().form_valid(form)

class PlanCreate(LoginRequiredMixin, CreateView):
    model = Plan
    fields = ["plan"]
    success_url = '/plans'

    def form_valid(self, form):
        if isinstance(self.request.user, User):
            form.instance.user = self.request.user
        else:
            print("Error: Invalid user instance")

        return super().form_valid(form)


def home(request):
    return render(request, 'home.html')

def checkins(request):
    current_date = date.today()
    print('Today is', current_date)

    if request.method == "POST":

        dietList = request.POST.getlist('diet')
        dietString = ', '.join(dietList)
        form = {
            'mood': request.POST.get('mood'),
            'sleep': request.POST.get('sleep_rating'),
            'diet': dietString,
            'exerciseType': request.POST.get('exerciseType'),
            'duration': request.POST.get('duration'),
            'intensity': request.POST.get('intensity'),
            'practices': request.POST.get('practices'),
            'improvements': request.POST.get('improvements'),
        }
        print("form: ")
        print(form)
        if all(form.values()):
            DailyCheckIn.objects.create(
                mood = form['mood'],
                sleep = form['sleep'],
                diet = form['diet'],
                exerciseType = form['exerciseType'],
                duration = form['duration'],
                intensity = form['intensity'],
                practices = form['practices'],
                improvements = form['improvements'],
                user = request.user
            )
            return redirect('/checkins')
        else:
            form = {}
        return redirect('/checkins/failed')
    return render(request, 'features/checkins.html', {'current_date': current_date})

    
def checkin_failed(request):
    return render(request, 'features/checkinfailed.html')


def journal(request):
    current_date = timezone.now().date()
    print('Today is', current_date)
    
    # Check if user is authenticated before filtering Journal objects
    if request.user.is_authenticated:
        user_entry = Journal.objects.filter(user=request.user, date=current_date).first()
    else:
        user_entry = None  # Or any other handling for unauthenticated users
        
    return render(request, 'features/journal.html', {'current_date': current_date, 'user_entry': user_entry})

def plans(request):
    current_date = date.today()
    print('Today is', current_date)
    
    # Check if user is authenticated before filtering Plan objects
    if request.user.is_authenticated:
        user_entry = Plan.objects.filter(user=request.user, date=current_date).first()
    else:
        user_entry = None  # Or any other handling for unauthenticated users
        
    return render(request, 'features/plans.html', {'current_date': current_date, 'user_entry': user_entry})




    # current_date = date.today()
    # # Get the latest plan entry for the current user
    # latest_plan = Plan.objects.filter(user=request.user).latest('id')
    # plans_today = [latest_plan] if latest_plan else []
    # return render(request, 'features/plans.html', {'current_date': current_date, 'plans': plans_today})


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



def upload_photo(request):
    if request.method == 'POST':
        form = PhotoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            photo = form.save(commit=False)
            photo.user = request.user 
            photo.save()
            return redirect('journal') 
    else:
        form = PhotoUploadForm()
    return render(request, 'journal.html', {'form': form})
