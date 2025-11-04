from django import forms
from .models import Setor

class SetorForm(forms.SetorForm):
    class Meta:
        model = Setor
        fields = '__all__'
        widgets = {
            'data': forms.DateInput(attrs={'type': 'datetime-local'})
        }