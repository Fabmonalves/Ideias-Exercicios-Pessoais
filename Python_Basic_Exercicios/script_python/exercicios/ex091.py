from random import randint
from operator import itemgetter
print('Valores sorteados:')
jogador = {}
ranking = []
for c in range(1,5):
    pc = randint(1,6)
    c = str(f'jogador{c}')
    jogador[c] = pc
    print(f'{c} tirou {pc} no dado')
print('-=-' *30)
print('RANKING DOS JOGADORES')
ranking = sorted(jogador.items(), key = itemgetter(1), reverse = True) # esse comando faz com que todos sejam tratados como uma lista 
for e, c in enumerate(ranking):
    print(f'{e + 1}° lugar: {c[0]} com {c[1]}.')
