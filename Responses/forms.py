from django import forms
from . import models

class VoteForm(forms.ModelForm):
    class Meta:
        model = models.Responses
        fields = ['movie_id', 'user_id', 'user_rate']
