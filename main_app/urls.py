from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkins/', views.checkins, name='checkins'),
    path('journal/', views.journal, name='journal'),
    path('plans/', views.plans, name='plans'),
    path('dailysummaries/', views.dailysummaries, name='dailysummaries'),
    path('accounts/', include('django.contrib.auth.urls')),
]

