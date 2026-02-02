#variaveis que utilizamos para receber os outros valores
media_idade = 0
homem_mais_velho = " "
idade_do_velho = -1
mulheres_menores = 0


for i in range (1, 4 + 1):
    
    nome = str (input (f'Digite o nome de uma pessoa qualquer {i}: '))
    idade = int (input (f'Digite a idade de uma pessoa qualquer {i}: '))
    sexo = str (input (f'Digite o sexo de uma pessoa qualquer {i} (M/F): '))
    sexo = sexo.upper()
    
    #aqui ele ta recebendo as idades e somando-as
    media_idade += idade
    
    #aqui ele ta vendo quem é o homem mais velho e recebendo o nome dele
    if sexo == 'M' and idade > idade_do_velho:
        idade_do_velho = idade
        homem_mais_velho = nome
    
    #aqui ele ta vendo a quantidade de mulheres que tem menos de 20 anos
    if sexo == 'F' and idade < 20:
        mulheres_menores += 1
   
#aqui ele vai organizar e printar tudo
media_idade = media_idade / 4
print (f'A idade média desse grupo é de: {media_idade}, ')

if homem_mais_velho:
    print (f'o nome do homem mais velho é: {homem_mais_velho}')
else: 
    print ('não a homens nesse grupo')

print (f'a quantidade de mulheres com menos de vinte anos é de: {mulheres_menores} ')