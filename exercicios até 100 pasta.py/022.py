nome_completo = input ('digite seu nome completo')
nome2 = len(nome_completo.replace(" ", ""))
nome3 = nome_completo.split()

print (f'seu nome com todas as letras maiusculas é {nome_completo.upper()}')
print (f'seu nome com todas as letras minusculas é {nome_completo.lower()}')
print (f'quantidade de letras sem considerar espaços: {nome2}')
print (f'seu primeiro nome é: {nome3[0]}')