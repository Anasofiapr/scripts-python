numeros = [[], [], []]

for linha in range(3):
    for coluna in range(3):
        numero = int(input (f'digite um numero inteiro para a posição [{linha}][{coluna}]: '))
        numeros[linha].append(numero)

print (f'Nosso 3x3 ficou assim: ')
for linha in numeros:
    for valor in linha:
        print (f'[{valor}]', end=' ')
    print ()
