def fatorial(num, show=False):
    """calculo fatorial
    Args:
        num (numero inteiro): O numero que serpa feito o fatorial
        show (bool, optional): _description_. Defaults to False.
    """
    from math import factorial
    print('-=' *30)
    if show == True:
        print(f'Fatorial {num}! = ', end ='')
        for c in range(0, num):
            if c == num - 1:
                print(f'{num - c} = ', factorial(num), end = ' ')
            else:
                print(f'{num - c} x', end = ' ')
    else:
        print(factorial(num))


numero = int(input('Digite um numero: '))  
while True:
    resp = str(input('Deseja mostrar o calculo? [S/N] ')).upper().strip()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('Por favor, apenas responder com S ou N: ')).upper().strip()[0]
        else:
            break
    if resp == 'S':
        show = True
        fatorial(numero, show)
        break
    if resp == 'N':
        show = False
        fatorial(numero, show)
        break

help(fatorial)