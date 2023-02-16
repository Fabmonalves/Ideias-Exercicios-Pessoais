from utilidadesCeV import moeda
num = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10% temoas {moeda.aumento(num, True)}')
print(f'Desconto de 10% temos {moeda.diminuir(num, True)}')