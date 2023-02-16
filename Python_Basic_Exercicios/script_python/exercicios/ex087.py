lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna = maior_valor = 0
for l in range(0,3):
    for c in range(0,3):
        lista[l][c] = int(input(f'Digite um valor [{l}, {c}] '))
for l in range(0,3):
    for c in range(0,3):
         print(f'[{lista[l][c]:^5}]', end = '')
    print()
for l in range(0,3):
    for c in range(0,3):
        if lista[l][c] % 2 == 0:
            soma_pares += lista[l][c]
        if c == 2:
            soma_coluna += lista[l][c]
        if l == 1:
            if lista[l][c] > maior_valor:
                maior_valor = lista[l][c]
print(f'A soma dos valores pares são {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_coluna}')
print(f'O maior valor da segunda linha é {maior_valor}')