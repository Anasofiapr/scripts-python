def gera_tabuada(
    numero_multiplicado:int,
    limite_tabuada:int
)->str:
    """
    Dado um número inteiro, retorna
    sua tabuada até o numero específicado
    partindo do 1
    """
    tabuada = ""
    for numero in range(1, limite_tabuada+1):
        tabuada += \
            f"{numero_multiplicado} x {numero} = {numero_multiplicado*numero}\n"
        print(tabuada)
    return tabuada


# numero_multiplicado = int(input("digite um numero a ser multiplicado: "))
# limite_tabuada = int(input("digite um numero limite para a tabuada: "))

# str_tabuada = gera_tabuada(numero_multiplicado, limite_tabuada)
# print(str_tabuada)

def anda_para_frente(numero_de_passos:int)->str:
    """
    Dado um número inteiro, retorna
    os passos feitos pelo usuário
    """
    passos = ""
    for passo in range(numero_de_passos):
        passos += "Deu um passo à frente\n"
    return passos

# numero_de_passos = int(input("digite um numero de passos: "))
# print(anda_para_frente(numero_de_passos))

geladeira = [
    "leite", "ovos", "queijo", "água", "iorgurt",
    "maçã", "banana", "pera", "caju", "mamão",
    "abacate", "superbonder"
]

item = input("Qual item deseja pegar na geladeira? ")
item = item.lower()

if item in geladeira:
    print(f"Pegou o item: {item}")
else:
    print(f"{item} não se encontra na geladeira.")

frase = input ('digite uma frase')
num_de_letras_da_frase = len(frase)

if len(frase) == 0:
    print ('a frase está vazia')
elif len(frase) < 21:
    print(f'o numero de letras da frase é {num_de_letras_da_frase} contando os espaços')
elif len(frase) > 20:
    print ('a frase tem mais de 20 letras')
elif frase.isspace():
    print (' a frase é feita de espaços')
else:
     print("A frase não existe ou não é uma frase.")