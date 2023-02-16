largura = float(input('Digite a largura da parece: '))
altura = float(input('Digite a altura da parece: '))
area = largura * altura
tinta = area / 2
print(' O murro tem a largura de {} e a altura de {}'.format(largura, altura))
print('Logo sua área é de {}m² \n Para cada 1L de tinta pegamos 2m²'.format(area))
print('Precisamos de {} litros de tinta para pintar a área de {}'.format(tinta, area))



