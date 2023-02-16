jogador = dict()
lista_princ = list()
lista_gols = list()
while True:
    jogador['nome'] = str(input('Nome do jogador: ')).title().strip()
    partidas = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))
    for c in range(0, partidas):
        lista_gols.append(int(input(f'Quantos gols na partida {c + 1}? ')))
    jogador['gols'] = lista_gols[:]
    jogador['total'] = sum(lista_gols)
    lista_princ.append(jogador.copy())
    jogador.clear()
    resp = str(input('Deseja cadastrar outro jogador? [S/N] ')).upper().strip()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('ERRO, Por favor, responder com S ou N: ')).upper().strip()[0]
        else:
            break
    if resp == 'N':
        break
print('-=' *40)
print('cod ', end='')
for i in lista_princ[0].keys():
    print(f'{i:<15}', end='')
print()
print('-=' *30)
for k, v in enumerate(lista_princ):
    print(f'{k:>3} ', end = '')
    for d in v.values():
        print(f'{str(d):<15}', end = '')
    print()
print('-=' *30)
while True:
    busca = int(input('Mostrar dados de qual jogador?(999 para parar) '))
    if busca == 999:
        break
    if busca >= len (lista_princ):
        print(f'ERRO! Não existejogador com código {busca}!')
    else:
        print(f' -- levantamento do jogador {lista_princ[busca]["nome"]}: ')
        for i, g in enumerate(lista_princ[busca]['gols']):
            print(f'  No jogo {i + 1} fez {g} gols.')
    print('-=' *30)
print('<< volte sempre >>')