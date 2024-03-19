from django import forms
from .models import Journal


class JournalEntryForm(forms.ModelForm):
    class Meta:
        model = Journal
        fields = ['dailyPrompt', 'freeWritte']