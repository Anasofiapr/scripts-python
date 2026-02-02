print ('pense numa parede que precisa ser pintada de tinta')
print ('você não sabe a quantidade de tinta para pintar essa parede,')
print ('mas sabe a altura e largura dela')

altura = float (input ('defina a altura em metros dessa parede'))
largura = float (input('defina a largura em metros desssa parede'))
area_que_tinta_cobre = int (2)
area = altura*largura  
quantidade_de_tinta = area/area_que_tinta_cobre

print (f'a área da parede é {area}m² e a quantidade de tinta nescessária é de {quantidade_de_tinta}L')