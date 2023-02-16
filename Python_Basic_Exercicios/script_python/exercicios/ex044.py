cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m',
         'roxo':'\033[35m'}

print('-=-' * 20)
print('{}Calculadora de descontos{}'.format(cores['roxo'], cores['limpa']))
print('-=-' * 20)

preco = float(input('Digite o preço do produto: '))
pagamento = str(input('Digite a forma de pagamento: ')).upper().strip()
cartao = 0
if 'CARTÃO' in pagamento or 'CARTAO' in pagamento:
    cartao = int(input('Sua escolha foi Cartão, deseja parcelar em quantas vezes?: '))
    if cartao == 1:
                print('À vista no cartão fica {:.2f} com desconto de {}"5%"{}'.format(preco - (preco * 5 / 100), cores['verde'], cores['limpa']))
    elif cartao == 2:
                print('Parcelado em {} fica o preço normal de {:.2f}'.format(cartao, preco))
    elif cartao >= 3: 
                print('Parcelando em {} a parcela fica {:.2f} com juros de {}"20%"{}'.format(cartao, preco + ((preco * 20 / 100) * cartao) , cores['vermelho'], cores['limpa']))
elif 'À VISTA' in pagamento or 'A VISTA' in pagamento or 'DINHEIRO' in pagamento or 'GRANA' in pagamento:
        print('À vista em dinheiro fica {:.2f} com {}"10%"{} de desconto'.format(preco - (preco * 10 / 100), cores['verde'], cores['limpa']))
        


