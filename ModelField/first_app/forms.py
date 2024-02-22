from django import forms
from first_app.models import Mymodel

class MyForms(forms.ModelForm):
    class Meta:
        model = Mymodel
        fields = '__all__'
        # exclude = ['roll']
        labels = {
            'name' : 'Student Name',
            'roll' : 'Student Roll'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'btn-primary'})
        }
