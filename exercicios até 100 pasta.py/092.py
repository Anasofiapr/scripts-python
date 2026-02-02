from datetime import date
cadastro_pessoa = {}

cadastro_pessoa['nome'] = input('seu nome: ')
cadastro_pessoa['sexo'] = input('Sexo: (M/F) ').upper()
cadastro_pessoa['dia_nascimento'] = int(input('Dia do seu aniversario: '))
cadastro_pessoa['mes_nascimento'] = int(input('mes do seu aniversario: '))
cadastro_pessoa['ano_nascimento'] = int(input('ano q vce nasceu: '))

if cadastro_pessoa['dia_nascimento'] >= date.today().day and cadastro_pessoa['mes_nascimento'] >= date.today().month:
    cadastro_pessoa['idade'] = date.today().year - cadastro_pessoa['ano_nascimento']
else:
    cadastro_pessoa['idade'] = date.today().year - cadastro_pessoa['ano_nascimento']
    cadastro_pessoa['idade'] -= 1

cadastro_pessoa['ctps'] = int(input('numero da ctps (0 = nao tenho): '))

if cadastro_pessoa['ctps'] == 0:
    print (f"""nome = {cadastro_pessoa['nome']}
idade = {cadastro_pessoa['idade']}
valor da ctps = {cadastro_pessoa['ctps']}""")

else:
    cadastro_pessoa['ano_contrata.'] = int(input('ano de contratação: '))
    cadastro_pessoa['salario'] = float(input('salário: '))

    if cadastro_pessoa['sexo'] == "F":
        cadastro_pessoa['aposentadoria'] = 62 - cadastro_pessoa['idade']
    else:
        cadastro_pessoa['aposentadoria'] = 65 - cadastro_pessoa['idade']

    for k, v in cadastro_pessoa.items():
        print(f'{k} tem o valor: {v}')






