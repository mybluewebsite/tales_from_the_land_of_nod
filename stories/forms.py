from .models import Suggestion
from django import forms


class SuggestionForm(forms.ModelForm):
    class Meta:
        model = Suggestion
        fields = ('body',)
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 4,
                'placeholder': 'Enter your suggestion here...'
            })
        }