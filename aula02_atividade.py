# Simulação de um sistema de suporte técnico simples

database = []


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



while True:
    print("\n--- Suporte Técnico ---")
    print("1. Novo Chamado")
    print("2. Consultar Chamados")
    print("3. Encerrar Chamado")
    print("0. Sair")
    escolha = input("Escolha uma opção (1-0): ")

    if escolha == '1':
        print("Abrindo novo chamado...")
        sala = input("Sala: ")
        problema = input("Problema: ")
        prioridade = input("Prioridade (de 1 a 5): ")
        registrar_chamado(sala, problema, prioridade)

    elif escolha == '2':
        print("Consultando chamados...")
        for c in database:
            print(f" Sala: {c['sala']},\n Problema: {c['problema']},\n Prioridade: {c['prioridade']},\n Status: {c['status']},\n\n")

    elif escolha == '3':
        print("Digite o número do chamado para encerrar...")
        numero = int(input("Chamado: "))
        if 0 <= numero < len(database):
            database[numero]['status'] = "Encerrado"
            print("Chamado encerrado com sucesso.")
        else:
            print("Chamado não encontrado.")
        
    elif escolha == '0':
        print("Saindo...")
        break

    else:
        print("Opção inválida.")