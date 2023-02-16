frase = str(input('Digite uma Frase qualquer: ')).lower().strip()
quantidade = len(frase)
print(frase.count('a'), 'Letras "a" na frase')
print(quantidade, 'de caracteres na frase')
print('A primeira posição que a letra "a" esteve ja frase é  {}'.format(frase.find('a', 0)))
print('A ultima posição que a letra "a" esteva na frease é {}'.format(frase.rfind('a', 0))) #esse comando rfind, faz com que a escolha seja feita da direita pra esquerda



