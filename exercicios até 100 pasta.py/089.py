boletim = []
nome = None
média = ()
nota1 = 0.0
nota2 = 0.0
executar = True

while executar:
    nome = input("nome do aluno: ")
    nota1 = float(input('nota do aluno: '))
    nota2 = float(input('nota do aluno: '))
    boletim.append([nome, nota1, nota2])

    continuar = input('voce deseja continuar? S/N: ').upper()
    if continuar == "N":
        executar = False

executar = True

for aluno in boletim:
    soma = aluno[1] + aluno[2]
    print (f'{aluno[0]} = {soma/2}')

while executar:
    ver_notas = input('ver as notas de quais alunos? (digite 999 pra parar) ')
    for aluno in boletim:
        if aluno[0] == ver_notas:
            print (f'nota = {aluno}')
    if ver_notas == '999':
        break

