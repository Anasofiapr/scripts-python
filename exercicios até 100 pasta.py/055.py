from math import inf

maior = 0
menor = float (inf)

for ps in range (1, 5 + 1):
    peso = float (input ('digite o peso de uma pessoa: '))
    if peso > maior:
        maior = peso
    if peso < menor:
       menor = peso
print (f'o maior peso é: {maior}kg e o menor é: {menor}kg')