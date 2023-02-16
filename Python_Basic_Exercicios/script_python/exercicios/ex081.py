lista = []
while True:
    lista.append(int(input('Digite um número: ')))
    lista.sort(reverse=True)
    continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while True:
        if continua not in 'SN':
            continua = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
        else:
            break
    if continua in 'N':
        break
print(f'Foram digitados {len(lista)} número.')
print(f'A lista de forma decrescente {lista}')
if 5 not in lista:
    print('O valor 5 não faz parte da lista!')
else:
    print(f'O valor 5 faz parte da lista')
    