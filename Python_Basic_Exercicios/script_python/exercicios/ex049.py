print('-=-' * 20)
print('\033[31mTabuada avançada\033[m')
print('-=-' * 20)

numero = int(input('Digite o número da Tabuada desejada: '))
for c in range(0, 11):
    print(f'{numero} x {c} = {numero * c}')
print('Fim da Tabuada!')

