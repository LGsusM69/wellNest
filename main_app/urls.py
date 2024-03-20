from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkins/', views.checkins, name='checkins'),
    path('journal/', views.journal, name='journal'),
    path('journal/create/', views.JournalCreate.as_view(), name='journal_create'),
    path('plans/', views.plans, name='plans'),
    path('plans/plan_form/', views.PlanCreate.as_view(), name='plan_create'),
    path('dailysummaries/', views.dailysummaries, name='dailysummaries'),
    path('accounts/', include('django.contrib.auth.urls')),
]


