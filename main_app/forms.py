from .models import Journal, Photo
from django.forms import ModelForm
from django import forms


class JournalEntryForm(ModelForm):
    class Meta:
        model = Journal
        # fields = ['freeWrite', 'user', 'photo'] # photo field was added by murs
        fields = ['freeWrite', 'photo'] # remove user VS



class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']

        