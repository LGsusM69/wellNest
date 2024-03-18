from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'home.html')

def dashboard(request):
    return render(request, 'features/dashboard.html')

def checkins(request):
    return render(request, 'features/checkins.html')

def journal(request):
    return render(request, 'features/journal.html')

def plans(request):
    return render(request, 'features/plans.html')

def dailysummaries(request):
    return render(request, 'features/dailysummaries.html')


