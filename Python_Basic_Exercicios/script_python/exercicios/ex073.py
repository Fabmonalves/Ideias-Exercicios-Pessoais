campeonato = ('palmeiras', 'santos', 'vasco da gama', 'gremio', 'flamengo', 'corinthians', 'internacional', 'cruzeiro', 'sao paulo', 'atletico mineiro', 'botafogo', 'fluminense', 'coritiba', 'bahia', 'goias', 'guarani', 'sport', 'portuguesa', 'atletico paranaense', 'vitoria')
print(f'Os primeiros 5 colocados foram {campeonato[0:5]}') #aqui estamos usando o sistema de fatiamento para pegar a colocação 0 da lista até a 6 ignorando a 6°
print(f'Os últimos 4 colocados foram {campeonato[-4:]}') # aqui estamos usando o sistema de fatiamento, esse negativo estamos dizendo para pegar contando pela direita 
print(f'Os times em ordem alfabetica: {sorted(campeonato)}') # esse comando sorted faz com que a tupla fique me ordem alfabetica, não da pra usar o sort porque o sort altera a variavel, e as duplas são inalteraveis, por isso o sorted, ele só organiza sem alterar a tupla 
print(f'O corinthians esta na {campeonato.index("corinthians") + 1}° posição') # nesse exemplo temos que colocar aspas duplas dentro da tupla index 