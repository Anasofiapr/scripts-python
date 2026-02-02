import random

numeros = tuple(random.randint(1,100) for numero in range(5))
maior = max(numeros)
menor = min(numeros)

print ('Os números sorteados foram:' , ", ".join(map(str, numeros)))
print (f"""O maior número sorteado foi: {maior}
O menor número sorteado foi: {menor}""")