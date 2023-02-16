nome = input('Qual o nome do aluno? ')
n1 = int(input('Digite a nota de português: '))
n2 = int(input('Digite a nota de Matemática: '))
media = (n1 + n2) /2
print(' O aluno {} recebeu a nota {} na materia de português e a nota {} na matéria de Matemática'.format(nome, n1, n2 ) ) 
print(' Valor total de notas do aluno {} é de {} e sua média é de {}'.format(nome, n1 + n2, media))