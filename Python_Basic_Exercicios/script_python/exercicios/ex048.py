cont = 0
soma = 0 
for c in range(1, 501):
    if c % 2 == 1 and c % 3 == 0:
        print(f'{c}', end = ' ' ) 
        cont += 1
        soma += c
print(f'\n A soma dos {cont} Números é {soma}')
        