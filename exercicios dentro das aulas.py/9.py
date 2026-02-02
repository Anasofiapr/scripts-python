frase1 = 'curso em video python'
print (frase1[9])
print (frase1[9:14])
print (frase1 [9:14:2])
print (frase1 [:5]) #ao contrário vai até o final
print (frase1 [9::3]) 
print (frase1[::4])

print ("""Desde o fim da Segunda Guerra Mundial,
os japoneses entraram em contato frequente com a cultura ocidental,principalmente com os Estados Unidos. 
A passagem da produção dos quadrinhos para os desenhos animados nos EUA chamou a atenção dos japoneses e,
em 1967, foram produzidos os primeiros desenhos animados criado por japoneses.
O primeiro anime de sucesso foi “Hakujaden” (“A Lenda da Serpente Branca”)""")

frase = input ('digite uma frase')
num_de_letras_da_frase = len(frase)

if len(frase) == 0:
    print ('a frase está vazia')
elif len(frase) < 21:
    print(f'o numero de letras da frase é {num_de_letras_da_frase} contando os espaços')
elif len(frase) > 20:
    print ('a frase tem mais de 20 letras')
else:
    print("A frase não existe ou não é uma frase.")

print (frase1.replace ('python', 'apple'))  
print (frase1)
frase1 = frase1.replace ('python', 'apple')
print (frase1)