from django.shortcuts import render, redirect, get_object_or_404
from .models import Setor
from .forms import SetorForm

def listar_setores(request):
    setores = Setor.objects.all()
    return render(request, 'setor/listar_setores.html', {'setores': setores})

def cadastrar_setor(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setor:listar_setores')
    else:
        form = SetorForm()
    return render(request, 'setor/cadastrar_setor.html', {'form': form})