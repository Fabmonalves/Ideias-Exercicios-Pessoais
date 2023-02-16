c = str(input('Digite o nome da Cidade: ')).capitalize().strip().split()
# Aqui estamos mandando a primeira palavra ser maiusculo e separando as palavras e tirando os espaços escedentes caso tenha, do começo e fim da frase

print('A cidade começa com o nome "Santo"? ')
print('A cidade começa com {} não começa com a palavra Santo, então a resposta é {}'.format(c[0],'Santo' in c))
