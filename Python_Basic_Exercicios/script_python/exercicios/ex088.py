from random import randint
from time import sleep
lista_num = []
temp = []
num = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 0
while tot < num:
    cont = 0
    while True:
        aleatorio = randint(1,60)
        if aleatorio not in temp:
            temp.append(aleatorio)
            temp.sort()
            cont += 1
        if cont >= 6:
            break
    lista_num.append(temp[:])
    temp.clear()
    tot += 1
for c in range(0, len(lista_num)):
    print(f'Jogo {c + 1}: {lista_num[c]}')
    sleep(1)
print('Fim do programa, boa sorte no jogo')