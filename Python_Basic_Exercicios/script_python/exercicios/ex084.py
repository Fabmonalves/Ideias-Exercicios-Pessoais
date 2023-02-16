cadastro = []
lista = []
maior = menor = 0
while True:
    cadastro.append(str(input('Digite o nome: ')))
    cadastro.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior = menor = cadastro[1] 
    else:
        if cadastro[1] > maior:
            maior = cadastro[1]
        if cadastro[1] < menor:
            menor = cadastro[1]
    lista.append(cadastro[:])
    cadastro.clear()
    continuar = str(input('Deseja continuar? [S/N] ')).title().strip()[0]
    while True:
        if continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).title().strip()[0]
        else: 
            break
    if continuar == 'N':
        break
print(f'Ao todo você cadastrou {len(lista)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de', end = ' ')
for p in lista:
    if p[1] == maior:
        print(f'[{p[0]}]', end = ' ')
print(f'\n O menor peso foi de {menor}Kg. Peso de', end = ' ')
for p in lista:
    if p[1] == menor:
        print(f'[{p[0]}]', end = ' ')

