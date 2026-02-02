# Solicita os valores das três retas
reta1 = float(input("Digite o valor da primeira reta: "))
reta2 = float(input("Digite o valor da segunda reta: "))
reta3 = float(input("Digite o valor da terceira reta: "))

# Verifica se as retas podem formar um triângulo usando a desigualdade triangular
if (reta1 + reta2 > reta3) and (reta1 + reta3 > reta2) and (reta2 + reta3 > reta1):
    print("As retas podem formar um triângulo.")
    
    # Determina o tipo de triângulo
    if reta1 == reta2 == reta3:
        print("O triângulo é equilátero.")
    elif reta1 == reta2 or reta1 == reta3 or reta2 == reta3:
        print("O triângulo é isósceles.")
    else:
        print("O triângulo é escaleno.")
else:
    print("As retas não podem formar um triângulo.")
