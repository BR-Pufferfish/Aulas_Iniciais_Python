from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World!</h1><p>Meu primeiro sistema Django está online.</p>")

# Nossa lista global (Banco de Dados em memória)
chamados = [
    {"lab": "Lab 01", "problema": "PC lento", "prioridade": "Média"},
]

def listar(request):
    # Lógica para listar os chamados em HTML
    html = "<h1>🖥️ HelpDesk - Lista de Chamados</h1><hr>"
    
    for i, c in enumerate(chamados):
        html += f"<p>ID: {i} | <b>{c['lab']}</b> - {c['problema']} ({c['prioridade']})</p>"
    
    html += "<br><a href='/novo/Lab02/Teclado/Alta/'>[Simular Novo Chamado]</a>"
    return HttpResponse(html)

def criar(request, lab, problema, prioridade):
    # Criando o dicionário e adicionando à lista
    novo = {
        "lab": lab,
        "problema": problema,
        "prioridade": prioridade
    }
    chamados.append(novo)
    
    return HttpResponse(f"✅ Chamado para o {lab} criado com sucesso! <br> <a href='/'>Voltar</a>")

def fechar(request, indice):
    del chamados[indice]
    
    return HttpResponse(f"✅ Chamado removido com sucesso! <br> <a href='/listar'>Voltar</a>")