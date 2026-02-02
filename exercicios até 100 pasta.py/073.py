time = input ('\033[0;32mEscolha um time de futebol!!\033[m ').upper()
print (' ')
vinte_primeiros_colocados = ( 
                                'PALMEIRAS', 'FLAMENGO', 'INTERNACIONAL', 'GRÊMIO', 'SÃO PAULO',
                                'ATLÉTICO‑MG', 'ATHLETICO‑PR', 'CRUZEIRO', 'BOTAFOGO', 'SANTOS',
                                'BAHIA', 'FLUMINENSE', 'CORINTHIANS', 'CHAPECOENSE', 'CEARÁ',
                                'VASCO', 'SPORT', 'AMÉRICA‑MG', 'VITÓRIA', 'PARANÁ CLUBE' 
)

print (f'\033[0;31m Os cinco primeiros colocados de 2018 foram:\033[m {', '.join(time.title() for time in vinte_primeiros_colocados[:5])}')
print (' ')
print (f'\033[0;32m Os 4 ultimos colocados de 2018 foram:\033[m {', '.join(time.title() for time in vinte_primeiros_colocados[-4:])}')
print (' ')
print (f'\033[0;31m Em ordem alfabética os times ficaram assim:\033[m {', '.join(time.title() for time in sorted(vinte_primeiros_colocados))}')
print (' ')

if time in vinte_primeiros_colocados:
    print (f'\033[0;32m O time do {time.title()}\033[m está na {vinte_primeiros_colocados.index(time)+1}ª posição nesse brasileirão de 2018')
    print (' ')
else:
     print (f'\033[0;31m O que vc escolheu\033[m ({time.title()}) não está nos vinte primeiros do brasileirão de 2018.')
     print (' ')