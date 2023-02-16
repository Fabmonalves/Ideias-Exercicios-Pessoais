import random
print('-=-' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('-=-' * 20)
cont = 0
while True:
    pc = random.randint(0, 10)
    usuario = int(input('Digite um valor: '))
    print('---' * 20)
    pi = str(input('Par ou Impar? [P/I] ')).upper().strip() [0]
    print('---' * 20)
    if (pc + usuario) % 2 == 0 and pi == 'P':
        print(f'Você jogou {usuario} e o computador {pc}. total de {usuario + pc}, deu PAR')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('-=-' * 20)
        cont += 1
    elif (pc + usuario) % 2 == 0 and pi == 'I':
        print(f'Você jogou {usuario} e o computador {pc}. total de {usuario + pc}, deu IMPAR')
        print('Você perdeu!')
        print('-=-' * 20)
        break
    elif (pc + usuario) % 2 == 1 and pi == 'I':
        print(f'Você jogou {usuario} e o computador {pc}. total de {usuario + pc}, deu PAR')
        print('Você venceu!')
        print('Vamos jogar novamente...')
        print('-=-' * 20)
        cont += 1
    elif (pc + usuario) % 2 == 1 and pi == 'P':
        print(f'Você jogou {usuario} e o computador {pc}. total de {usuario + pc}, deu IMPAR')
        print('Você perdeu!')
        print('-=-' * 20)
        break
print(f'Game Over, você venceu {cont} vezes')