soma = 0

for numero in range (0, 501):
    if numero % 2 != 0 and numero % 3 == 0:
        soma += numero
print (f'a soma dos numeros impares multiplos de tres entre 1 e 500 são: {soma}')