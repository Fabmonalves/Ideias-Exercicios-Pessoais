import datetime
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'amarelo':'\033[33m'} # colocando as cores em uma lista para poder usar no codigo todo 
         
print('-=-' * 20)
print('{}Federação Nacional de Natação{}'.format(cores['verde'], cores['limpa']))
print('-=-' * 20)

ano = int(input('Digite o ano de nascimento: '))
ano_atual = datetime.date.today().year
idade = ano_atual - ano
if idade <= 9:
    print('Sua idade é {}, esta na categoria {}MIRIM{}'.format(idade,cores['amarelo'],cores['limpa']))
elif idade >= 10 and idade <= 14:
    print('Sua idade é {}, esta na categoria {}INFANTIL{}'.format(idade,cores['amarelo'],cores['limpa']))
elif idade >= 15 and idade <= 19:
    print('Sua idade é {}, esta na categoria {}JUNIOR{}'.format(idade,cores['verde'],cores['limpa']))
elif idade == 20 and idade <= 25:
    print('Sua idade é {}, esta na categoria {}SÊNIOR{}'.format(idade,cores['azul'],cores['limpa']))
else:
    print('Sua idade é {}, esta na categoria {}MASTER{}'.format(idade,cores['vermelho'],cores['limpa']))
