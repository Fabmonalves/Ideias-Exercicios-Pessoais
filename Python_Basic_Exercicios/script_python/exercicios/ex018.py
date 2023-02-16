import math
angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo)) #nesse ex estamos convertendo o angulo para radianus e depois pegando o seno do angulo do trisngulo
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print (' O ânfulo de {} tem o SENO de {:.2f}'.format(angulo, seno))
print ( 'O ânfulo de {} tem o COSSENO de {:.2f}'.format(angulo, cosseno))
print ( 'O ânfulo de {} tem o TANGENTE de {:.2f}'.format(angulo, tangente))

