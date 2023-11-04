from django import forms
from .models import Alert

class AlertForm(forms.ModelForm):
    class Meta:
        model = Alert
        fields = ['name', 'description', 'base', 'quote', 'threshold_value']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Ex: Alert for Bitcoin Drop'}),
            'description': forms.Textarea(attrs={'placeholder': 'Describe the conditions for the alert.'}),
            'base': forms.Select(attrs={'class': 'form-control'}),
            'quote': forms.Select(attrs={'class': 'form-control'}),
            'threshold_value': forms.NumberInput(attrs={'placeholder': 'Enter threshold value'}),
        }
