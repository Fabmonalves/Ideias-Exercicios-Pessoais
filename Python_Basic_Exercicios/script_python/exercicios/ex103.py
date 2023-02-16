def ficha(jogador = '<desconhecido>', gol = 0): #coloquei aqui parametros opcionais
        print(f' O jogador {jogador} fez {gol} gol(s) no campeonato')
    
    
nome = str(input('Nome do Jogador: ')).title().strip()
num_gol = str(input('Número de Gols: '))
if num_gol.isnumeric():
    num_gol = int(num_gol)
else:
    num_gol = 0
if nome.strip() == '':
    ficha(gol = num_gol)
else:
    ficha(nome, num_gol)
    