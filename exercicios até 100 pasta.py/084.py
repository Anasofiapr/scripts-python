#This variable is responsible for control the iterations of the while loop below
executar = True
cadastro = []
continuar = "" #Defines if the program keeps adding new users
maior_peso = None
maior_peso_nome = None
menor_peso = None
menor_peso_nome = None
parar = True

while executar:

    if continuar in ("S", "SIM"):
        print("Insira os dados do novo usuário: ")
        continuar = ""

    while parar: #ENQUANTO VERDADEIRO
        try:
            nome = input('Nome: ')
            if nome.isnumeric():
                raise AttributeError
        except AttributeError:
            print ("isso não é um nome, tente novamente...")
        else:
            break

    while parar:
        try:
            peso = float(input('Peso: '))
            if type(peso) != float:
                raise ValueError
            elif peso < 0:
                raise TypeError
        except ValueError:
            print ("isso não é um valor, tente novamente...")
        except TypeError:
            print ("Não tem como ser um numero negativo, digite um peso real.")
        else:
            break

    cadastro.append([nome, peso])

    while continuar not in ("SIM", "NÃO", "NAO", "S", "N"):
        continuar = input(
            'Deseja continuar? Responda apenas com "Sim" ou "Não": '
        ).upper()

    if continuar in ("NÃO", "NAO", "N"):
        executar = False

#cadastro = [["Ana", 50], ["Andre", 15], ["Mari", 40]]

for nome, peso in cadastro:

    #Maior peso
    if not maior_peso or maior_peso < peso:
        maior_peso = peso
        maior_peso_nome = nome

    #Menor peso
    if not menor_peso or menor_peso > peso:
        menor_peso = peso
        menor_peso_nome = nome

print("Maior peso: ", maior_peso, maior_peso_nome)
print("Menor peso: ", menor_peso, menor_peso_nome)
