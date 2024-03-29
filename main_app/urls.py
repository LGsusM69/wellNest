from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('checkins/', views.checkins, name='checkins'),
    path('checkins/failed', views.checkin_failed, name='checkin_failed'),
    path('journal/', views.journal, name='journal'),
    path('journal/create/', views.JournalCreate.as_view(), name='journal_create'),
    path('plans/', views.plans, name='plans'),
    path('plans/create/', views.plan_create, name='plan_create'),
    path('dailysummaries/', views.dailysummaries, name='dailysummaries'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('dailysummaires/', views.upload_photo, name='upload_photo'),

]

# Add media URL pattern for development environment
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

