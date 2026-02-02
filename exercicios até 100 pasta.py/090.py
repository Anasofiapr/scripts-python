cadastro_aluno = {}
cadastro_aluno['nome'] = input('Nome do aluno: ')
cadastro_aluno['média'] = float(input('Média do aluno: '))

if cadastro_aluno['média'] >= 7:
    cadastro_aluno['situação'] = 'Aprovado'
else:
    cadastro_aluno['situação'] = 'Reprovado'

for k, v in cadastro_aluno.items():
    print (f'{k} = {v}')
