"""nome = input ('diga o nome de uma cidade qualquer ')
lower = nome.lower()
santo = (lower.count ('santo',0,6))
if santo == 0:
    print ('tem santo no primeiro nome da cidade!')
else:
    print ('essa cidade não tem santo no primeiro nome')"""

nome_cidade = input ('diga o nome de uma cidade qualquer ')
lower_2 = nome_cidade.lower()
fatiamento = lower_2[0:6]
print ("se for dito False é por que não tem santo na primeira palavra e True é pq tem")
print ('santo' in fatiamento)

