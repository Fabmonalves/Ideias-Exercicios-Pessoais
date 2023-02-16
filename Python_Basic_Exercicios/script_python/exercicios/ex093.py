jogador = dict()
lista_gols = list()
jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    lista_gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
jogador['gols'] = lista_gols[:]
jogador['total'] = sum(lista_gols)
print('-=' *30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' *30)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f' => Na partida {c + 1}, fez {lista_gols[c]} gols.')
print(f'Foi um total de {jogador["total"]} gols')