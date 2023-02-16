import datetime
ano_atual = datetime.date.today().year
lista_nome_menor = []
lista_ano_menor = []
lista_nome_maior = []
lista_ano_maior = []
for c in range(0, 7):
    nome = str(input('Me informe seu nome: ')).title()
    ano = int(input('Me informe o ano de seu nascimento: '))
    if ano_atual - ano >= 21:
        lista_nome_maior.append(nome)
        lista_ano_maior.append(ano)
    else: 
        lista_nome_menor.append(nome)
        lista_ano_menor.append(ano)
        
print(f'''\033[33m{len(lista_ano_maior)}\033[m pessoas que foram cadastradas estão na maior idade
Essas pessoas são \033[32m{lista_nome_maior}\033[m''')
print(f'''\033[33m{len(lista_ano_menor)}\033[m pessoas que foram cadastradas estão na menor idade
Essas pessoas são \033[32m{lista_nome_menor}\033[m''')

#resolução do professor

atual = datetime.date.today().year
totmaior = 0
totmenor = 0
for pess in range (1,8):
    nasc = int(input(f'Em que ano a {pess}° pessoa nasceu?'))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'E também tivemos {totmenor} pessoas menres de idade')

