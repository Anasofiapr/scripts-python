numeros = [[], []]

for num in range (0, 7):
    numero_digitado = int (input ("digite um numero inteiro: "))

    if numero_digitado % 2 == 0:
        numeros[0].append(numero_digitado)
        #print (numeros)
    else:
        numeros[1].append(numero_digitado)
        #print (numeros)

numeros[0].sort()
numeros[1].sort()

print (f"""Valores pares: {numeros[0]}
Valores impares: {numeros[1]}""")
