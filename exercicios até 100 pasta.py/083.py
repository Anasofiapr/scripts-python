contador = 0
expressao = input ("digite uma expressão numérica com parenteses: ")

for letra in expressao:
    if letra == "(":
        contador += 1
    elif letra == ")":
        contador -= 1

if contador != 0:
    print ("Sua expressão numérica está errada.")
else:
    print ("Sua expressão numérica está correta.")
