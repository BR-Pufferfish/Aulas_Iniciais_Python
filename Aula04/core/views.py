from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Chamado, Categoria


# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"id": 1, "laboratorio": "Lab 01", "descricao": "PC lento", "prioridade": "Alta"},
    {"id": 2, "laboratorio": "Lab 02", "descricao": "Impressora sem tinta", "prioridade": "Média"},
    {"id": 3, "laboratorio": "Lab 03", "descricao": "Sem conexão com a internet", "prioridade": "Baixa"},
]

# Novas listas globais para categorias
categorias = [
    {"id": 1, "nome": "Hardware"},
    {"id": 2, "nome": "Software"},
    {"id": 3, "nome": "Rede"},
]

def home(request):
    return render(request, 'core/home.html')

def novo_chamado(request): 
    if request.method == "POST":
        laboratorio = request.POST.get('laboratorio')
        descricao = request.POST.get('descricao')
        prioridade = request.POST.get('prioridade')
        id_categoria = request.POST.get('categoria')

        # Buscamos o objeto real da categoria no banco
        categoria_selecionada = Categoria.objects.get(id=id_categoria)

        Chamado.objects.create(
            laboratorio=laboratorio, 
            descricao=descricao, 
            prioridade=prioridade,
            categoria=categoria_selecionada # Passamos o objeto, não o texto!
        )
        return redirect('/listar-chamados')

    if request.method == "GET":
        print("chegou um get")
        categorias = Categoria.objects.all()
        return render(request, 'core/novo_chamado.html', {'categorias': categorias})
   

def fechar(request, id):
    chamado = Chamado.objects.get(id=id)
    chamado.delete()
    print(f"Fechando chamado {chamado.id} - {chamado.descricao}")
    return redirect('/listar-chamados')

def listar_chamados(request):
    chamados = Chamado.objects.all() 
    return render(request, 'core/listar_chamados.html', {"chamados": chamados})




# Novas views para categorias

def listar_categorias(request):
    return render(request, 'core/listar_categorias.html', {"categorias": categorias})

def nova_categoria(request):
    if request.method == "POST":
        nome = request.POST.get('nome')
        categorias.append({
            "id": len(categorias) + 1,
            "nome": nome
        })
        # salvar meus dados
        return redirect('/listar-categorias')
    return render(request, 'core/nova_categoria.html')

def excluir_categoria(request, id):
    for categoria in categorias:
        if categoria["id"] == id:
            categorias.remove(categoria)
            break
    return redirect('/listar-categorias')

def editar_categoria(request, id):
    categoria = Categoria.objects.get(id=id)
    if request.method == "POST":
        #salvar as alterações
        categoria.nome = request.POST.get('nome')
        categoria.save()
        return redirect('/listar-categorias')

    if request.method == "GET":
        return render(request, 'core/editar_categoria.html', {'categoria': categoria})