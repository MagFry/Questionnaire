from django import forms
from . import models

class NameForm(forms.ModelForm):
    class Meta:
        model = models.Users
        fields = ['user_name']
