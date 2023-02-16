salario = float(input('Digite o salário: '))
aumento = float(input('Digite o aumento: '))
final = salario + ((salario*aumento) /100)
print('O salário {} com o aumento dos {} fica {}'.format(salario, aumento, final))