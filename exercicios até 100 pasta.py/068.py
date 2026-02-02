import random
import logging

ganhou = ()
perdeu = ()

logging.basicConfig(level=logging.INFO)

par_ou_impar = input ('par ou impar? (P/I) ')
numero = int (input ('digite um numero: '))

logging.info(f"{par_ou_impar=} | {numero=}")

# Jogamos contra o bot (python)
python = ""
# Python escolhe um numero aleatório
numero_python = random.randint(0, 10)
#Somamos o numero escolhido aleatoriamente e o numero escolhido pelo usuario
soma = numero_python + numero
logging.info(f"{numero_python=} | {soma=}")

if par_ou_impar == "P":
    python = "I"

if soma % 2 == 0:
    print (f'você jogou {numero} e PAR, eu joguei {numero_python} e IMPAR, a soma é de {soma}, VOCÊ GANHOU!')
elif par_ou_impar == 'I':
    python = 'P'

if soma % 2 != 0:
    print (f'você jogou {numero} e IMPAR, eu joguei {numero_python} e PAR, a soma é de {soma}, EU GANHEI!')
