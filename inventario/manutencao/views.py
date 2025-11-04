from django.shortcuts import render, redirect, get_object_or_404
from .models import Manutencao
from .forms import ManutencaoForm

def listar_manutencoes(request):
    manutencoes = Manutencao.objects.all()
    return render(request, 'manutencao/listar_manutencoes.html')

def cadastrar_manutencao(request):
    if request.method == 'POST':
        form = ManutencaoForm(request.POST)
        if form.is_valid():
            form.save
            return redirect('manutencao:listar_manutencao') # ! Checar singular
    else:
        form = ManutencaoForm()