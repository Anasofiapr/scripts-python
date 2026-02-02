import time

print ('joãozinho quer saber a média da sua nota em matematica até agora') 
time.sleep(2)
print ('ele ja fez duas provas de matematica')
time.sleep(2)

np1 = int (input ('determine a nota da primeira prova de joãozinho: '))
np2 = int (input ('determine a nota da segunda prova de joãozinho: '))
med = (np1 + np2) /2

print ('a média de joãozinho nas duas provas foi: {}'.format (med))
