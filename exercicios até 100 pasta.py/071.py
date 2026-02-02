print (""" 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
                        ANA'S BANCO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""")

valor_sacado = int(input('Escolha um valor a ser sacado: R$'))
valor = valor_sacado
cinquenta = 0
vinte = 0
dez = 0
um = 0

while valor >= 50:
    valor -= 50
    cinquenta += 1

while valor >= 20:
    valor -= 20
    vinte += 1

while valor >= 10:
    valor -= 10
    dez += 1

while valor >= 1:
    valor -= 1
    um += 1

print (f'o valor sacado é: {valor_sacado}')
print(f"Notas de R$50: {cinquenta}")
print(f"Notas de R$20: {vinte}")
print(f"Notas de R$10: {dez}")
print(f"Notas de R$1: {um}") 
