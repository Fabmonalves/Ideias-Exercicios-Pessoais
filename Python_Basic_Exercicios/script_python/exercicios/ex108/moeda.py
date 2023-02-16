def metade(n = 0):
    n = n / 2
    return n


def dobro(n = 0):
    n = n * 2
    return n


def aumento(n = 0):
    n = ((n * 10) / 100) + n
    return n

def diminuir(n = 0):
    n = n - ((n * 10) / 100)
    return n


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')