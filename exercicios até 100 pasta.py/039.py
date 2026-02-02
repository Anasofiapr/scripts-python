dia = int (input ('digite o dia do seu nascimento: '))
mes = int (input ('digite o mes do seu nascimento: '))
ano = int (input ('digite o ano do seu nascimento: '))

dia_atual = int (input ('digite a data de hj: '))
mes_atual = int (input ('digite o mes de hj: '))
ano_atual = int (input ('digite o ano de hj: '))


idade = ano_atual - ano
antes_da_idade = 18 - idade
depois_da_idade = idade - 18

if idade < 18:
    print (f'daqui a {antes_da_idade} anos você se alistará no serviço militar')
elif idade == 18:
    print ('já é hora de se alistar no serviço militar!')
else: 
    print (f'já passou {depois_da_idade} anos da idade de se alistar ao serviço militar')