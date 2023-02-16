def soma(a, b):
    s = a + b
    print(s)

    
# Programa principal
soma(5, 4)
soma(4, 9)
soma(1, 2)

def contador(*num): #esse comando é chamado de desempacotamento, diz que serão entregues varios parametros, não se sabe quantos
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')

    
contador(1, 2, 3, 4)
contador(4, 5)
contador(1, 8, 7, 9, 7, 7, 5, 6, 54)


def somas(*valores): #esse comando é chamado de desempacotamento, diz que serão entregues varios parametros, não se sabe quantos
    s = 0
    for num in valores:
        s+=num
    print(f'Somando os valores {valores} temos {s}')


somas(5, 6)
somas(4, 5, 6, 7)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *=2
        pos += 1
        
        
valores = [6, 3, 4, 7, 15, 2]
dobra(valores)
print(valores)
        