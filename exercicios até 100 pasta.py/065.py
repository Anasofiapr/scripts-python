from math import inf

maior = 0
menor = float (inf)
numero = 0
soma = 0
count = 0
resposta = 'sim'

while resposta != 'não':
    numero = float (input ('digite um numero: '))
    soma += numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
    count += 1
    resposta = str (input ('gostaria de continuar (sim/não)? '))
    resposta = resposta.lower()

media =  soma / count
print (f'o maior numero é: {maior} o menor é: {menor} e a média é: {media}')