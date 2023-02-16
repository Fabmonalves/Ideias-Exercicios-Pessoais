listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.00, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
cont = 0
print('-' * 40)
print(f'{"Listagem de preços":^40}') #essa formatação é pra dar estilo, estou dizendo para deixar centralizado ^ com 40 espaços
print('-' * 40)
for c in range(0, len(listagem)):
    if c % 2 == 0:
        print(f'{listagem[c]:.<30}', end = '') # aqui estou dizendo para colocar 30 . começanco pela esquerda 
    else:
        print(f'R$ {listagem[c]:>7.2f}') # nesse caso estamos falando para começar da direita e dando um espaçamento de 7 e colocando 2 elementos na unidade fazendo parecer um float, sempre colocar : antes pra poder fazer esses comandos 