from django import forms
from .models import Show

class showForm(forms.ModelForm):
    class Meta:
        model = Show
        fields = '__all__'