
numeros = [[], [], []]
pares = 0
terceira_coluna = 0

for linha in range(3):
    for coluna in range(3):
        numero = int(input (f"digite um numero inteiro para a posição [{linha}][{coluna}]: "))
        numeros[linha].append(numero)
        if numero % 2 == 0:
            pares += numero

print (f'Nosso 3x3 ficou assim: ')
for linha in numeros:
    for valor in linha:
        print (f'[{valor}]', end=' ')
    print ()

print ("----"*20)
for coluna in range (3):
    terceira_coluna += numeros[coluna][2]

maior = numeros[1].index(max(numeros[1]))

print (f"""A soma dos numeros pares resulta em: {pares}
A soma da terceira coluna fica: {terceira_coluna}
o maior numero da segunda linha é: {numeros[1][maior]}""")
