lista = []
impares = []
pares = []

while True:
    numero = int (input ("digite um numero inteiro: "))

    lista.append(numero)

    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

    continuar = input ("deseja continuar? (Sim ou Não?) ").upper()

    while continuar != "SIM" and continuar != "NÃO" and continuar != "NAO":
        continuar = input ("deseja continuar? (responda apenas com: Sim ou Não) ").upper()
        if continuar == 'SIM' or continuar == 'NÃO' or continuar == "NAO":
            break

    if continuar != 'SIM':
        break

print (f"""A lista de numeros digitados ficou: {lista}
A lista de numeros pares ficou: {pares}
A lista de numeros impares ficou: {impares} """)
