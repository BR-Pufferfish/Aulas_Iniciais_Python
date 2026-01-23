# Simulação de um sistema de suporte técnico simples
from chamados_funcoes import encerrar_chamado, consultar_chamados, registrar_chamado


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
        consultar_chamados()

    elif escolha == '3':
        encerrar_chamado()
        
    elif escolha == '0':
        print("Saindo...")
        break

    else:
        print("Opção inválida.")