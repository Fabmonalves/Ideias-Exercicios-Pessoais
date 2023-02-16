oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = ( oposto ** 2 + adjacente ** 2  ) ** (1/2) # para sabermos o vqalor da hipotenusa, temos que fazer a raiz quadrada das somas dos lados do quadrado
print(' A hipotenusa vai medir {:.2f}, usando o cauculo a mão '.format(hipotenusa))

import math
hi = math.hypot(oposto, adjacente) # dessa forma calculamos a hipotenusa usando a biblioteca math usandio a função hypot
print('a hipotenusa vai medir {:.2f}, usando a biblioteca math'.format(hi)) 
