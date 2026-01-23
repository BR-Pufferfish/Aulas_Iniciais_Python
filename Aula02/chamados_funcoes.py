database = []


def consultar_chamados(database):
    print("Consultando chamados...")
    index = 0
    for c in database:
        print(f"Chamado {index}:\n Sala: {c['sala']}\n Problema: {c['problema']}\n Prioridade: {c['prioridade']}\n Status: {c['status']}\n")
        index += 1



def encerrar_chamado(database):
    print("Digite o número do chamado para encerrar...")
    numero = int(input("Chamado: "))
    if 0 <= numero < len(database):
        database[numero]['status'] = "Encerrado"
        print("Chamado encerrado com sucesso.")
    else:
        print("Chamado não encontrado.")



def registrar_chamado(sala, problema, prioridade):
    if prioridade not in ['1', '2', '3', '4', '5']:
        print("Prioridade inválida. Chamado não registrado.")
        return False

    chamado = {
        "sala": sala,
        "problema": problema,
        "prioridade": prioridade,
        "status": "Aberto"
    }

    database.append(chamado)
    print("Chamado registrado com sucesso.")
    return True