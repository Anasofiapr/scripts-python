numeros = []
num1 = int (input (f'digite um numero para a posição 0: '))
numeros.append(num1)
maior = num1
menor = num1
maior_posicao = 0
menor_posicao = 0
for num in range (1, 5):
    num1 = int (input (f'digite um numero para a posição {num}: '))

    numeros.append(num1)

    if num1 > maior:
        maior = num1
        maior_posicao = num
    if num1 < menor:
        menor = num1
        menor_posicao = num

print (f"""A lista ficou assim: {", ".join(map(str,numeros))}
O maior numero é o numero {maior} na posição {maior_posicao}
O menor numero é o numero {menor} na posição {menor_posicao}""")
