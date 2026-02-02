import random
import logging

sim_não = ''
contador_de_ganhos = 0
contador_de_ganhos_do_python = 0

logging.basicConfig(level=logging.INFO)

while True:
    # Entrada do jogador: P ou I
    escolha_do_jogador = input('Par ou ímpar? (P/I): ').upper()
    while escolha_do_jogador not in ('P', 'I'):
        escolha_do_jogador = input('Escolha inválida! Digite "P" para Par ou "I" para Ímpar: ').upper()

    # Número do jogador
    numero = int(input('Digite um número: '))

    logging.info(f"{escolha_do_jogador=} | {numero=}")

    # Número aleatório do computador
    numero_python = random.randint(0, 10)

    # Soma dos números
    soma = numero + numero_python
    logging.info(f"{numero_python=} | {soma=}")

    # Verifica se a soma é par ou ímpar
    if soma % 2 == 0:
        resultado = 'P'  # Par
    else:
        resultado = 'I'  # Ímpar 

    resultado = 'P' if soma % 2 == 0 else 'I'   

    # Verifica se o jogador ganhou ou perdeu
    if escolha_do_jogador == resultado:
        print(f'Você jogou {numero} e escolheu {"PAR" if escolha_do_jogador == "P" else "ÍMPAR"}.')
        print(f'Eu joguei {numero_python}. A soma foi {soma} ({ "PAR" if resultado == "P" else "ÍMPAR" }).')
        contador_de_ganhos += 1
        print('VOCÊ GANHOU!')
    else:
        print(f'Você jogou {numero} e escolheu {"PAR" if escolha_do_jogador == "P" else "ÍMPAR"}.')
        print(f'Eu joguei {numero_python}. A soma foi {soma} ({ "PAR" if resultado == "P" else "ÍMPAR" }).')
        contador_de_ganhos_do_python += 1
        print('VOCÊ PERDEU!')
    
    sim_não = input ('Vc deseja continuar? sim ou não? ').upper()
    if sim_não == 'NÃO':
        break
print (f'Vc ganhou {contador_de_ganhos} veses e eu ganhei {contador_de_ganhos_do_python} veses!')