from .models import Suggestion
from django import forms


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('body',)