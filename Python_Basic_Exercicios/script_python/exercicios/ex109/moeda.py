def metade(n = 0, formato = False):
    n = n / 2
    return n if not formato else moeda(n)


def dobro(n = 0, formato = False):
    n = n * 2
    return n if not formato else moeda(n)


def aumento(n = 0, formato = False):
    n = ((n * 10) / 100) + n
    return n if not formato else moeda(n) #retorne n se formato for false, senão faça moeda(n) 

def diminuir(n = 0, formato = False):
    n = n - ((n * 10) / 100)
    return n if formato == False else moeda(n) #retorne n se formato for igual a false, caso contrario faça moeda(n)


def moeda(n = 0, moeda = 'R$'):
    return f'{moeda}{n:.2f}'.replace('.',',')