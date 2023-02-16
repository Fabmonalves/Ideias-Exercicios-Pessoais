import datetime
from time import sleep
print('-=-' * 20)
print('Alistamento militar')
print('-=-' * 20)

ano_atual = datetime.date.today().year
ano = int(input('Digite aqui o ano de nascimento: '))
idade = ano_atual - ano

print('Você nasceu no ano de {} e estamos hoje no ano {}, sua idade é {}'.format(ano, ano_atual,  idade))
sleep(2)
if idade < 18:
    print('Você tem {} anos, falta apenas {} anos para se alistar'.format(idade, 18 - idade)) 
elif idade == 18:
    print('Sua idade é {}, esta na hora de se alistar!'.format(idade))
elif idade >= 19:
    print(' Você ja passou da idade para se alistar, passou {} anos, corre atraz disso agora!'.format(idade - 18))
    
    
    