import random
print ("""vamos jogar um jogo! Você tentará adivinhar um numero entre 1 e 10 que eu estou pensando,
vc terá infinitas tentativas e no final te mostrarei quantas tentativas vc precisou para ganhar!""")

contagem = 0
numero_python = random.randint (1,11)

numero_pessoa = 0
while numero_pessoa != numero_python:
    numero_pessoa = int (input ('digite um numero aleatório entre 1 e 10!!! '))
    if numero_pessoa == numero_python:
        print ('uau vc acertou!!')
        contagem += 1
    else: 
        print ('você errou! tente novamente!')
        contagem += 1

print (f'você precisou de {contagem} tentativa(s)!')