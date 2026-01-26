import json
database = []


def consultar_chamados():
    print("Consultando chamados...")
    index = 0
    for c in database:
        print(f"Chamado {index}:\n Sala: {c['sala']}\n Problema: {c['problema']}\n Prioridade: {c['prioridade']}\n Status: {c['status']}\n")
        index += 1



def encerrar_chamado():
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



def exportar_chamados(tipo_exportar):
    match tipo_exportar:

        case 0:
            with open('chamados_exportados.json', 'w') as f:
                json.dump(database, f, indent=4)
            print("Chamados exportados com sucesso para 'chamados_exportados.json'.")

        case 1:
            abertos = [c for c in database if c['status'] == 'Aberto']
            with open('chamados_abertos.json', 'w') as f:
                json.dump(abertos, f, indent=4)
            print("Chamados abertos exportados com sucesso para 'chamados_abertos.json'.")
    
        case 2:
            encerrados = [c for c in database if c['status'] == 'Encerrado']
            with open('chamados_encerrados.json', 'w') as f:
                json.dump(encerrados, f, indent=4)
            print("Chamados encerrados exportados com sucesso para 'chamados_encerrados.json'.")
        
        case _:
            print("Opção de exportação inválida.")


