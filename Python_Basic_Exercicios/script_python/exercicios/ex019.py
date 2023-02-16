import random
al1 = str(input('Primeiro aluno(a): '))
al2 = str(input('Segundo aluno(a): '))
al3 = str(input('Terceiro aluno(a): '))
al4 = str(input('Quarto aluno(a): '))
lista = [al1, al2, al3, al4]
print(' O aluno escolido foi {}'.format(random.choice(lista))) # esse choice é uma função da biblioteca random para escolher, nesse caso que é uma escolha aleatoria de quem esta dentro da variavel lista, toda lista tem que estar entre couchetes, tipo os arrays de JS 
