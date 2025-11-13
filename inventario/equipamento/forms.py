from django import forms
from .models import Equipamento

class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = '__all__'
    '''    widgets = {
            'data': forms.DateInput(attrs={'type': 'datetime-local'}),
        } '''