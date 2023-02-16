from random import randint
from time import sleep


def sorteia():
    print('Sorteando 5 valores da lista: ', end='')
    sort = 0
    while len(numero) < 5:
        sort = randint(0,10)
        if sort not in numero:
            numero.append(sort)
    for i in numero:     
        print(i, end=' ', flush = True)
        sleep(0.5)
    print('PRONTO!')
    
    
def somaPar():
    soma = 0
    for i in numero:
        if i % 2 == 0:
            soma += i
    print(f'A soma dos pares dentro da lista {numero}, temos {soma}')
    
    
numero = list()
sorteia()
somaPar()