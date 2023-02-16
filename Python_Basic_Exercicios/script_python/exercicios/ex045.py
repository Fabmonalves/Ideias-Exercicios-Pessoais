import random
from time import sleep
cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m'}
print('-=-' * 20)
print('{}Bem vindo ao Jogo de JOQUEM PO!{}'.format(cores['azul'], cores['limpa']))
print('-=-' * 20)

print('Escolhendo entre {}PEDRA{}, {}PAPEL{} e {}TESOURA{}....'.format(cores['amarelo'], cores['limpa'], cores['roxo'], cores['limpa'], cores['verde'], cores['limpa']))
computador = random.choice(['PEDRA', 'PAPEL', 'TESOURA'])
'''Da também para criar uam variavel e colocar o pedra , papel e teseolta em uma lista  como no exemplo: lista:(pedra,papel,tesolra) e usar o ramdom.randint(lista[0, 2]) para fazer a escolha randomica '''
sleep(3)
jogador = str(input('Pronto, adivinhe o que escolhi >.<: ')).upper().strip()

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print ('-=-' *20 )
if jogador == computador:
    print('Empatamos, nos dois escolhemos {}'.format(jogador))
elif jogador == 'TESOURA' and computador == 'PAPEL' or jogador == 'PEDRA' and computador == 'TESOURA' or jogador == 'PAPEL' and computador == 'PEDRA':
    print('Nossa, você é bom nisso, {} ganha de {}, você {}GANHOU{}!'.format(jogador, computador, cores['verde'], cores['limpa']))
elif computador == 'TESOURA' and jogador == 'PAPEL' or computador == 'PEDRA' and jogador == 'TESOURA' or computador == 'PAPEL' and jogador == 'PEDRA':
    print('hahah, {} ganha de {}, ganhei e você {}PERDEU{}!'.format(computador, jogador, cores['vermelho'], cores['limpa']))
print ('-=-' *20 )
