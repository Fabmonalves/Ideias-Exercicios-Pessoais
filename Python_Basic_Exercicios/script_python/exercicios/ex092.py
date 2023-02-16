from datetime import datetime
cadastro = dict()
ano_atual = datetime.now().year
cadastro['Nome'] = str(input('Nome: ')).title().strip()
nasc = int(input('Ano de nascimento: '))
cadastro['Idade']= ano_atual - nasc
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] == 0:
    print('-=' *30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')
else:
    cadastro['Contratação'] = int(input('Ano de contratação: '))
    cadastro['Salário'] = float(input('Salário: R$'))
    cadastro['Aposentadoria'] = cadastro['Idade'] + (35 - (ano_atual - cadastro['Contratação'])) 
    print('-=' *30)
    for k, v in cadastro.items():
        print(f' - {k} tem o valor {v}')