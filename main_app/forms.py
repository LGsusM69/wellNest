from .models import Photo
from django.forms import ModelForm
from django import forms

class PhotoUploadForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']

        