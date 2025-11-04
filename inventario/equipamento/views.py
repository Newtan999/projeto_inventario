from django.shortcuts import render, redirect, get_object_or_404
from .models import Equipamento
from .forms import EquipamentoForm

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/listar_equipamentos.html', {'equipamentos': equipamentos})

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento:listar_equipamentos') #! Checar singular
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/cadastrar_equipamento.html', {'form': form})