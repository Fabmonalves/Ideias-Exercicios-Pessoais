lista = []
lista_pares = []
lista_impares = []
while True:
    lista.append(int(input('Digite um número: ')))
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while True:
        if continuar not in 'SN':
            continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        else:
            break
    if continuar in 'N':
        break 
print(f'A lista completa é {lista}')
for c in lista:
    if c % 2 == 0:
        lista_pares.append(c)
    else:
        lista_impares.append(c)
print(f'A lista de pares é {lista_pares}')
print(f'A lista de impares é {lista_impares}')