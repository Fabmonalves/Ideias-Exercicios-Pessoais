n = str(input('Digite seu nome completo: ')).title().strip()
nome = n.split()
print('Seu nome completo é {}'.format(n))
print('Seu primeiro nome é: {}'.format(nome[0]))
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) # dessa forma estamos dizendo para a variavel nome pegar o len , comprimento total dos caracteres e tirando 1 para compensar o valor zero 