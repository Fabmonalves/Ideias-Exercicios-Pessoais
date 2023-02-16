inicio = int(input('Dinite o Inicio da PA: '))
pulo = int(input('Digite o valor do pulo de sua PA: '))
decimo = inicio + (10 - 1) * pulo #esse aqui é a formula da matemática para pegarmos o decimo termo de uma PA
for c in range(inicio, decimo + pulo, pulo):
    print(f'{c}', end = ' -> ')
print('Fim da sua PA!')