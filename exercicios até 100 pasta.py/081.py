lista = []
contador = 0
resposta = ''
while True:

    numero = int (input ('digite um numero: '))

    lista.append(numero)

    parar = input ('deseja continuar? s/n ').upper()
    #só pra ver se a pessoa vai realmente responder com sim ou nao.
    while parar != 'SIM' and parar != 'NÃO' and parar != 'S' and parar != 'N':
        parar = input ('deseja continuar? responda apenas com: s/n ').upper()
        if parar == 'SIM' or parar == 'NÃO' or parar == 'S' or parar == 'N':
            break

    if parar != 'SIM' and parar != 'S':
        break

if 5 in lista:
    resposta = "foi"
else:
    resposta = "não foi"

print (f"Foram digitados: {len(lista)} numero(s)")

lista.sort(reverse=True)

if len(lista) == 1:
    print (f"A lista em ordem decrescente ficou: {lista}")
else:
    print (f"A lista em ordem decrescente ficou: {lista}")

print (f"e o numero 5 {resposta} adicionado na lista.")
