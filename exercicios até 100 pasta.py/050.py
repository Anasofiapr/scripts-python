soma = 0

for recebe in range (0, 6):
    numero = int (input ('digite um numero inteiro: '))
    if numero % 2 == 0:
        soma += numero
    
print (f'a soma de todos os numeros pares é de: {soma}')