maiores = 0
menores = 0

for oi in range (1, 7 + 1):
    idade = int (input ('qual é a sua idade? '))
    if idade >= 18: 
        maiores += 1
    else: 
        menores += 1
print (f'a quantidade de maiores de idade é de {maiores} e de menores de idade é de {menores}')