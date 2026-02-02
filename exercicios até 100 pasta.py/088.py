from random import randint

print ('='*5, 'MEGA CENA', '='*5)
num_jogos = int (input ("Quantos jogos você quer que eu sorteie? "))
jogo = []
num_random = []

for no in range(num_jogos):
    for nothing in range(6):
        jogo.append(randint(1, 61))

for i in range(0, len(jogo), 6):
   num_random.append(jogo[i:i+6])

print (f"Seu jogo aleatorio ficou: {num_random}")
