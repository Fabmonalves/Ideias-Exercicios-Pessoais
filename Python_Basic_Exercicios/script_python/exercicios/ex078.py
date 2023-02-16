num = []
for n in range(0, 5):
    num.append(int(input((f'Digite um valor para a posição {n}: '))))
print('-=-' * 20)
print(f'Você digitou os valores {num}')
print(f'O maio valor digitado foi o {max(num)} nas posições ' , end = ' ')
for ordem, valor in enumerate(num):
    if valor == max(num):
         print(f'{ordem :.<4}', end = ' ')
print(f'\nO menor valor digitado foi o {min(num)} nas posições ', end = ' ')
for ordem, valor in enumerate(num):
    if valor == min(num):
        print(f'{ordem :.<4}', end = ' ')
    