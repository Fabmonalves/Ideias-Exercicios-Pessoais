pares = []
num_tupla = (int(input('Digite um número: ')),
int(input('Digite outro número: ')),
int(input('Digite outro número: ')),
int(input('Digite o último número: ')))
print(num_tupla)
print(f'o valor 9 apareceu {num_tupla.count(9)} vezes')
if 3 in num_tupla:
        print(f'O valor 3 apareceu na {num_tupla.index(3)}° posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for c in range(0,len(num_tupla)):
    if num_tupla[c] % 2 == 0:
        pares.append(num_tupla[c])
print(f'Os valor pares digitados foram {pares}')
print('FIM do programa')
