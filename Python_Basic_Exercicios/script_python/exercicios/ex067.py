#forma feita pelo professor, usando o comando for para simplificar 
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' *30)
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n * c}')
    print('-' *30)
print(f'Valor informado é {n} (negativo)!')
print('Programa tabuada encerrado. volte sempre!')

#feita sem o for por mim
tab = int(input('Quer ver a tabuada de qual valor? '))
c = 0
while True:
    if tab < 0:
        break
    else:
        print(f'{tab} x {c} = {tab * c}')
        c += 1
        if c > 10:
            print('-=-' * 20)
            tab = int(input('Quer ver a tabuada de qual valor? '))
            print('-=-' * 20)
            c = 1
print(f'Valor informado é {tab} (negativo)!')
print('Programa tabuada encerrado. volte sempre!')
    
