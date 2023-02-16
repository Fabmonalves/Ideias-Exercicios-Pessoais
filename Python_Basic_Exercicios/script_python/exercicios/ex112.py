from utilidadesCeV import dados
from utilidadesCeV import moeda

num = dados.leiaDinheiro('Digite o preço: R$')
moeda.resumo(num, 80, 35)
