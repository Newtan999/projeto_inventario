from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Equipamento
from .forms import EquipamentoForm

def listar_equipamentos(request):
    equipamentos = Equipamento.objects.all()
    return render(request, 'equipamento/form_equipamentos.html', {'equipamentos': equipamentos})

def cadastrar_equipamento(request):
    if request.method == 'POST':
        form = EquipamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('equipamento:listar_equipamentos', {'form': form})
    else:
        form = EquipamentoForm()
    return render(request, 'equipamento/form_equipamentos.html', {'form': form})

def excluir_equipamento(request, id):
    equipamento = get_object_or_404(Equipamento, id=id)
    if request.method == 'POST':
        equipamento.delete()
        return redirect('listar_equipamentos')
    
    return render(request, 'equipamento/confirmar_exclusao.html', {
        'objeto': equipamento.nome,
        'voltar_url': reverse('listar_equipamentos')
    })