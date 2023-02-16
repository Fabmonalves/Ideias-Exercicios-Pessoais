sal = float(input('Digite o valor do Salario: '))
if sal > 1250.00:
    print('Seu salário é {}, com o aumento fica {}, aumento de 10% por conta do valor do salario'.format(sal, sal + (sal * 10 / 100)))
else:
    print('Seu salário é {}, com o aumento fica {}, aumento de 15% por conta do valor do salario'.format(sal, sal + (sal * 15 / 100)))
print('---FIM---')