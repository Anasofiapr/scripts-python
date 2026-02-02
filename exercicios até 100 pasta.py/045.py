import random
jokenpo = ['pedra', 'papel', 'tesoura']
escolha = random.choice(jokenpo)
print ('vamos jogar jokenpô')
jogada = input ('faça sua jogada: ')
jogada = jogada.lower()


if escolha == jogada:
    print (f'eu jogo: {escolha}, empatamos!')
elif escolha == 'pedra' and jogada == 'tesoura':
    print (f'eu jogo: {escolha}, ganhei! Pedra quebra tesoura!')
elif escolha == 'tesoura' and jogada == 'papel':
    print (f'eu jogo: {escolha}, e tesoura corta papel, ganhei!')
elif escolha == 'papel' and jogada == 'pedra':
    print (f'eu jogo: {escolha}, ganhei! papel enrola a pedra!')
else:
    print (f'eu jogo: {escolha}, você ganhou!!!')

#deu certo de primeira!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!