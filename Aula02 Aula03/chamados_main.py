# Simulação de um sistema de suporte técnico simples
from chamados_funcoes import encerrar_chamado, consultar_chamados, registrar_chamado, exportar_chamados


while True:
    print("\n--- Suporte Técnico ---")
    print("1. Novo Chamado")
    print("2. Consultar Chamados")
    print("3. Encerrar Chamado")
    print("4. Exportar Chamados")
    print("0. Sair")
    escolha = int(input("Escolha uma opção (1-0): "))

    match escolha:

        case 1:
            print("Abrindo novo chamado...")
            sala = input("Sala: ")
            problema = input("Problema: ")
            prioridade = input("Prioridade (de 1 a 5): ")
            registrar_chamado(sala, problema, prioridade)

        case 2:
            consultar_chamados()

        case 3:
            encerrar_chamado()

        case 4:
            print("Selecione quais chamados deseja exportar:")
            print("0. Todos os chamados")
            print("1. Chamados abertos")
            print("2. Chamados encerrados")
            tipo_exportar = int(input("Escolha uma opção (0-2): "))

            exportar_chamados(tipo_exportar)
            
        case 0:
            print("Saindo...")
            break

        case _:
            print("Opção inválida.")