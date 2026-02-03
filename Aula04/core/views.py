from django.http import HttpResponse
from django.shortcuts import render, redirect
# from .models import Chamado
from django.contrib.auth.decorators import login_required

chamados = [
    {"id": 1, "laboratorio": "Lab 01", "problema": "Computador não liga", "prioridade": "Alta", "data_criacao": "2024-01-10 14:30"},
    {"id": 2, "laboratorio": "Lab 02", "problema": "Internet lenta", "prioridade": "Média", "data_criacao": "2024-01-11 09:15"},
    {"id": 3, "laboratorio": "Lab 03", "problema": "Impressora sem tinta", "prioridade": "Baixa", "data_criacao": "2024-01-12 11:45"},
]

atendentes = [
    {"id": 1, "nome": "Ana Carolina Machado"},
    {"id": 2, "nome": "Marcelo"},
]


def home(request):
    return render(request, "core/home.html" ) 

#@login_required
def novo_chamado(request):
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        problema = request.POST.get('problema')
        prioridade = request.POST.get('prioridade')

        print("chegou um post")
        print(f"Laboratório: {laboratorio}, Descrição: {problema}")

        # Chamado.objects.create(laboratorio=laboratorio, problema=problema, prioridade=prioridade)
        
       
        return redirect('/listar')

    if request.method == "GET":
        print("chegou um get")
        return render(request, 'core/novo_chamado.html')


# Ainda retorna HttpResponse
def fechar_chamado(request, id):
    # chamado = Chamado.objects.get(id=id)
    # chamado.delete()
    # print(f"Fechando chamado {chamado.id} - {chamado.problema}")
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")


#@login_required
def listar(request):
    # Busca TODOS os registros do banco de dados
    # chamados = Chamado.objects.all() 
    return render(request, 'core/listar.html', {"chamados": chamados})


def listar_atendentes (request):
    return render(request, 'core/listar_atendentes.html', {"atendentes": atendentes})