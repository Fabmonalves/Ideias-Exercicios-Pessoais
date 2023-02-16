velocidade = float(input('Digite a velocidade do Carro: '))
if velocidade > 80:
    print('Velocidade do Carro ultrapassou a velocidade de 80km')
    print('''Você foi multado, valor da multa é R${:.2f};
    O valor é correspondente a R$ 7,00 reias por Km rodados acima do permitido'''.format((velocidade - 80) * 7))
else:
    print('Tenha um bom dia, dirija com segurança')