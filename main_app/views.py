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
from datetime import datetime, time



# Create your views here.

class JournalCreate(LoginRequiredMixin, CreateView):
    model = Journal
    fields = ["freeWrite", "photo"]
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


#class PlanCreate(LoginRequiredMixin, CreateView):
    #model = Plan
    #fields = ["plan"]
    #success_url = '/plans'


def home(request):
    return render(request, 'home.html')

def checkins(request):
    current_date = date.today()
    print('Today is', current_date)

    existing_checkin = DailyCheckIn.objects.filter(user=request.user, date=current_date).first()

    if request.method == "POST":

        dietList = request.POST.getlist('diet')
        dietString = ', '.join(dietList)

        practicesList = request.POST.getlist('practices')
        practicesString = ', '.join(practicesList)
        form = {
            'mood': request.POST.get('mood'),
            'sleep': request.POST.get('sleep'),
            'diet': dietString,
            'exerciseType': request.POST.get('exerciseType'),
            'duration': request.POST.get('hours'),
            'intensity': request.POST.get('intensity'),  
            'practices': practicesString,  
             'improvements': request.POST.get('improvements')
     

        }
        print("form: ")
        print(form)
        if all(form.values()):

            if existing_checkin:
                #update
                existing_checkin.mood = form['mood']
                existing_checkin.sleep = form['sleep']
                existing_checkin.diet = form['diet']
                existing_checkin.exerciseType = form['exerciseType']
                existing_checkin.duration = form['duration']
                existing_checkin.intensity = form['intensity']
                existing_checkin.practices = form['practices']
                existing_checkin.improvements = form['improvements']
                try:
                    existing_checkin.save()

                except:
                    print('failed')
                return redirect('/checkins')
            
            else:
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


                #lo mismo
        else:
            form = {}
        return redirect('/checkins/failed')
    return render(request, 'features/checkins.html', {'current_date': current_date})

    
def checkin_failed(request):
    return render(request, 'features/checkinfailed.html')


def journal(request):
    current_date = timezone.now().date()
    print('Today is', current_date)
    if request.user.is_authenticated:
        user_entry = Journal.objects.filter(user=request.user, date=current_date).first()
    else:
        user_entry = None 
        
    return render(request, 'features/journal.html', {'current_date': current_date, 'user_entry': user_entry})

def plans(request):
    current_date = date.today()
    print('Today is', current_date)
    if request.user.is_authenticated:
        user_entry = Plan.objects.filter(user=request.user, date=current_date).first()
    else:
        user_entry = None 
        
    return render(request, 'features/plans.html', {'current_date': current_date, 'user_entry': user_entry})

def plan_create(request):
    current_date = date.today()
    print('Today is', current_date)

    if request.method == "POST":

        print('method is POST')
        #print(request.POST.date, request.POST.plan)
        print(request.POST.getlist('plan'))

        req_planList = request.POST.getlist('plan')
        req_date = request.POST.get('date')
        timeList = ['06:00', '06:30', '07:00', '07:30',
                    '08:00', '08:30', '09:00', '09:30',
                    '10:00', '10:30', '11:00', '11:30',
                    '12:00', '12:30', '13:00', '13:30',
                    '14:00', '14:30', '15:00', '15:30',
                    '16:00', '16:30', '17:00', '17:30',
                    '18:00', '18:30', '19:00', '19:30',
                    '20:00', '20:30', '21:00', '21:30',
                    '22:00', '22:30']
        user = request.user
        user_id = request.user.id
        print('id: ')
        print(request.user.id)

        for index in range(0, 34):
            print('cangrejo')    

            timeString = timeList[index]
            hour, minute = map(int, timeString.split(':'))
            timeVar = time(hour=hour, minute=minute)   
            # Skip empty plans
            if req_planList[index] == "":
                print(index)
                continue
            
            # Check if a plan already exists for the given date and time
            existing_plan = Plan.objects.filter(date=req_date, time = timeVar).first()
            if existing_plan:
                # Update existing plan
                existing_plan.plan = req_planList[index]
                existing_plan.save()
            else:
                # Create new plan

                Plan.objects.create(plan = req_planList[index], date = req_date, time = timeVar, user_id=user_id)
            
            # Repeat the process for half-hour plans
        
        # Redirect to a success URL or return a response
        return redirect('/plans')  # Adjust this to your success URL
        

    return render(request, 'main_app/plan_form.html', {'current_date': current_date})

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
