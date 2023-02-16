print(input.__doc__)
help(print)


def contador(i, f, p):
    """_summary_

    Args:
        i (_type_): inicio da contagem
        f (_type_): fim da contagem
        p (_type_): passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end=' ')
        c+=p
    print('FIM!')


contador(2,10,2)

help(contador)
help