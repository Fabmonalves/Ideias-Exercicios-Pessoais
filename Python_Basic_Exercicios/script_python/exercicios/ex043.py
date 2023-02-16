cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'verde':'\033[32m,',
         'amarelo':'\033[33m',
         'azul':'\033[34m',
         'roxo':'\033[35m'}

print('-=-' * 20)
print('{}Calculadora de IMC{}'.format(cores['roxo'], cores['limpa']))
print('-=-' * 20)

peso = float(input('Digite aqui o seu peso: '))
altura = float(input('Digite aqui sua altura: '))
imc = peso / (altura ** 2 ) # Como calcular o IMC exemplo? Resultado de imagem para como calcular o IMC de uma pessoa O IMC é calculado dividindo o peso pela altura elevada ao quadrado. 

print(' Seu IMC é {:.2f}'.format(imc))

if imc < 18.5:
    print('Esta {}ABAIXO{} do peso'.format(cores['vermelho'], cores['limpa']))
elif imc >= 18.5 and imc <= 25:
    print('Esta no peso {}IDEAL{}'.format(cores['verde'],cores['limpa']))
elif imc > 25 and imc <= 30:
    print('Esta no {}SOBREPESSO{}'.format(cores['amarelo'],cores['limpa']))
elif imc > 30 and imc <= 40:
    print('Esta na {}OBESIDADE{}'.format(cores['vermemho'],cores['limpa']))
elif imc > 40:
    print('Esta na \033[7;31mOBESIDADE MORBIDA{}!'.format(cores['limpa']))