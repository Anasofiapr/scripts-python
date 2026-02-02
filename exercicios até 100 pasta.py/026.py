frase = input ('digite uma frase: ')
frase = frase.lower()

if 'a' in frase:
    print (f'essa frase  tem: {frase.count('a')} letras a')
    print (f'a primeira letra se encontra no espaço: {frase.find('a')}')
    print (f'a ultima letra se encontra no espaço: {frase.rfind ('a')}')
else: 
    print ('não tem nenhuma letra a na frase')