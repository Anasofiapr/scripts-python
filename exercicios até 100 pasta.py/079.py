#cria a lista numeros
numeros = []

#inicia o loop
while True:


    try:
        # Vai tentar colocar o treco pra int
        num = int (input ('Digite um numero: '))
        numero = int(num)

        # Caso der erro (spoiler se nn for numero vai dar) vai entrar aqui e nn vai deixar o programa travar
    except ValueError:
        num = int (input("numero invalido insira outro numero: "))

    if num in numeros:
        print ('Esse numero já existe na lista! Digite outro por favor.')
    else:
        numeros.append(num)

    continuar = input ('quer continuar? (N/S) ').lower()
    while continuar != "n" and continuar != "s":
        continuar = input ('Não consegui entender! Você gostaria ou não de continuar? (S/N) ').lower()

    if continuar == "n":
        break

print (f'Você digitou os valores: {sorted(numeros)}')
