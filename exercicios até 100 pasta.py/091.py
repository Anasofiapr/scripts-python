from random import randint

jogadores = {}

#Loop to save random numbers to each player
for i in range(1, 10):
    jogadores[i] = randint(1, 100)

sorted_dict = dict(sorted(jogadores.items(), key=lambda x: x[1], reverse=True))

for pos, (k, v) in enumerate(sorted_dict.items(), 1):
    print (f'O {pos}º lugar vai para o: jogador_{k}, com o numero: {v}.')
