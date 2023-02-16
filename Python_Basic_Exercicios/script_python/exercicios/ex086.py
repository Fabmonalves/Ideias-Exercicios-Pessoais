tabela = [[], [], []]
for c in range(0,3):
    tabela[0].append(int(input(f'Digite um valor para [0 , {c}] ')))
for c in range(0,3):
    tabela[1].append(int(input(f'Digite um valor para [1 , {c}] ')))
for c in range(0,3):
    tabela[2].append(int(input(f'Digite um valor para [2 , {c}] ')))
for l in range(0,3):
    for c in range(0,3):
        print(f'[{tabela[l][c]:^5}]', end = '')
    print() #esse formato de for dentro de for pode ser usado para armazenar os valores tbm 