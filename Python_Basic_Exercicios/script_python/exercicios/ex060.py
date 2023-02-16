numero = int(input('Digite um número: '))
cont = numero
resultado = numero
while cont != 1:
    resultado = resultado * (cont - 1)
    cont -= 1
print(f'O fatorial do numero {numero}! é {resultado}')

#forma simplificado de fazer o calculo de fatorial usando a biblioteca math
import math
continuar = ''
while continuar != 'N':  
    num = int(input('Digite um número: '))
    print(f'O fatorial de {num}! é {math.factorial(num)}')
    continuar = str(input('Deseja calcular o fatorial de outro numero? [S/N]: ')).upper()
print('Fim do programa')

