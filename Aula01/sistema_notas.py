nomealuno = input("Nome do aluno: ")
nomedisciplina = input("Disciplina: ")
nomeprofessor = input("Professor: ")
listaNotas = []
aviso = "Digite uma nota entre 0 e 10." 

while len(listaNotas) < 4:
    print(aviso)
    nota = float(input(f"Digite a nota {len(listaNotas) + 1}: "))
    if 0 <= nota <= 10:
        listaNotas.append(nota)
    else:
        print(aviso)
media = sum(listaNotas) / len(listaNotas)

print(f" Aluno: {nomealuno} \n Disciplina: {nomedisciplina} \n Professor: {nomeprofessor} \n A média é: {media:.2f}")