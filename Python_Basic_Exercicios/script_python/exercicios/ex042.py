cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m]',
         'azul':'\033[34m',
         'roxo':'\033[35m'
         }

print('-=-' * 20)
print('{}Medidas para Triângulos{}'.format(cores['roxo'],cores['limpa']))
print('-=-' * 20)

a = float(input('Digite o parametro A: '))
b = float(input('Digite o paramtro B: '))
c = float(input('Digite o paramtro C: '))

print('''Parametro A: {}
Parametro B: {}
Parametro C: {}'''.format(a, b, c))

if a < b + c and b < a + c and c < a + b:
    print('Com esse parametros conseguimos formar um triangulo')
    if a == b or b ==  c or a == c:
        print('O triangulo formado é  {}isosceles{}'.format(cores['azul'],cores['limpa']))
    elif a == b and a == c and b == c:
        print('O triangulo formado é   {}equilátero{}'.format(cores['amarelo'],cores['limpa']))
    elif a != b and a != c and b != c:
        print('O triangulo formado é   triangulo {}escaleno{}'.format(cores['verde'],cores['limpa']))
else:
    print('Com esses parametros {}não formamos um triangulo{}!'.format(cores['vermelho'],cores['limpa']))