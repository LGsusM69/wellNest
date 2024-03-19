from .models import Journal
from django.forms import ModelForm


class JournalEntryForm(ModelForm):
    class Meta:
        model = Journal
        fields = ['dailyPrompt', 'freeWrite']
        