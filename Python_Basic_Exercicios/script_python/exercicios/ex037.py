from time import sleep
cores = {'limpa':'\033[m', 
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m'}

print('-=-' * 20)
print('{}Conversor de Números Inteiros{}'.format(cores['azul'], cores['limpa']))
print('-=-' * 20)
sleep(1)
cliente = int(input('Digite um número para conversão: '))
print('-=-' *10)
print('[1] {}BINARIO{}'.format(cores['amarelo'], cores['limpa']))
print('[2] {}OCTAL{}'.format(cores['verde'], cores['limpa']))
print('[3] {}HEXADECIMAL{}'.format(cores['vermelho'], cores['limpa']))
print('-=-' * 10)
sleep(1)
numero = int(input('Escolha uma das opções para conversão: '))

if numero == 1: 
    print('A conversão do número {} para {}BINARIO{} é {}'.format(cliente, cores['amarelo'], cores['limpa'], bin(cliente)[2:]))
elif numero == 2:
    print('A conversão do número {} para {}OCTAL{} é {}'.format(cliente, cores['verde'], cores['limpa'], oct(cliente)[2:]))
elif numero == 3:
    print('A conversão do número {} para {}HEXAADECIMAL{} é {}'.format(cliente, cores['vermelho'], cores['limpa'], hex(cliente)[2:]))
else:
    print('Opção invalida!')