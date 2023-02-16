nome = str(input('Digite o seu Nome: ')).title().strip().split() 
# nesse caso fizemos a mesma coisa com os demais, mas usamos o comando title nele porque o silva pode estar na frente, meio ou atraz, o title faz a primeira letra de cada palavra ser maiuscula
print('O nome tem "Silva" nele?')
print('Silva' in nome)