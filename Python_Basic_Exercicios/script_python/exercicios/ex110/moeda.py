def metade(n = 0, formato = False):
    n = n / 2
    return n if not formato else moeda(n)


def dobro(n = 0, formato = False):
    n = n * 2
    return n if not formato else moeda(n)


def aumento(n = 0, aum = 10, formato = False):
    n = ((n * aum) / 100) + n
    return n if not formato else moeda(n) #retorne n se formato for false, senão faça moeda(n) 

def diminuir(n = 0, dim = 5, formato = False):
    n = n - ((n * dim) / 100)
    return n if formato == False else moeda(n) #retorne n se formato for igual a false, caso contrario faça moeda(n)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')


def resumo(n = 0, aum = 10, dim = 5):
    print('-=' *16)
    print('RESUMO DO VALOR'.center(30))
    print('-=' *16)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True)}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'Aumento de {aum}%: \t{aumento(n, aum, True)}')
    print(f'dominuição de {dim}%: \t{diminuir(n, dim, True)}')
    print('-=' *16)