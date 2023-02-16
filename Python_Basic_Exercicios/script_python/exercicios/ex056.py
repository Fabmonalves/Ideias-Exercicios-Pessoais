lista_nomes = []
lista_idade = []
lista_M = []
lista_F = []
velho = 0
for c in range(0,5):
    nome = str(input('Digite seu Nome: ')).title()
    lista_nomes.append(nome)
    idade = int(input('Digite sua idade: '))
    lista_idade.append(idade)
    sexo = str(input('Digite "F" para feminimo ou "M" para masculino: ')).upper()
    if sexo == str('F') and idade < 20:
        lista_F.append(sexo)
    elif sexo == str('M') and idade > velho:
        lista_M.append(sexo)
        velho = idade
        nome_velho = nome
print(lista_nomes)
print(lista_idade)
print(lista_F)
print(lista_M)
print(f'A media de idade de todos é {sum(lista_idade) / len(lista_idade)}')
print(f'O homem mais velho é {nome_velho} com {velho} anos')
print(f'São {len(lista_F)} mulheres com idade inferiror a 20 anos')