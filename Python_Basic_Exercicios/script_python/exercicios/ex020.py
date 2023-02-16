import random

n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('Quarto aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) # esse comando em especifico para embaralhar a lista, deve ser colocado  fora do format, dentro não deu certo 
print('A ordem de apresentação será \n {}'.format(lista))