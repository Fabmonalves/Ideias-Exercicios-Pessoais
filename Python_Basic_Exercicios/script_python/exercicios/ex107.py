from utilidadesCeV import moeda
num = float(input('Digite um preço: '))
print(f'A metade de R${num} é R${moeda.metade(num)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'Aumentando 10% temoas R${moeda.aumento(num)}')
print(f'Desconto de 10% temos R${moeda.diminuir(num)}')