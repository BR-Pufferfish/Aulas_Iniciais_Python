from django.http import HttpResponse
from django.shortcuts import render, redirect

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"id": 1, "lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]

def home(request):
    return render(request, "core/home.html")

def baseHtml(request):
    return render(request, "core/base.html")

def listar(request):
    return render(request, "core/listar.html", {"chamados": chamados})


def novoChamado(request, lab, problema, prioridade):
    if request.method == "POST":
        print('Um request.POST:')
        
        novo = {
        "id": len(chamados) + 1,
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
        }
        chamados.append(novo)

        return redirect('/listar')

        

    if request.method == "GET":
        print('request.GET:', request.GET)
        return redirect('/listar')


# def novoChamado(request):
#     return render(request, "core/novoChamado.html")

def criar(request, lab, problema, prioridade):
    # Criando o dicionário e adicionando à lista
    novo = {
        "id": len(chamados) + 1,
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
    }
    chamados.append(novo)
    
    return HttpResponse(f"✅ Chamado para o {lab} criado com sucesso! <br> <a href='/'>Voltar</a>")

def fechar(request, indice):
    del chamados[indice]
    
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")