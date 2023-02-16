from utilidadesCeV import moeda
num = float(input('Digite um preço: '))
print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10% temoas {moeda.moeda(moeda.aumento(num))}')
print(f'Desconto de 10% temos {moeda.moeda(moeda.diminuir(num))}')