# lendo nome, idade e sexo até que op usuario diga pra parar
formulario_temp = dict()
lista_princ = list()
lista_idade = list()
lista_fem = list()
while True:
    formulario_temp["nome"] = str(input('Nome: ')).title().strip()
    formulario_temp["idade"] = int(input(f'Idade de {formulario_temp["nome"]}: '))
    formulario_temp["sexo"] = str(input(f'Sexo [M/F]: ')).upper().strip()[0]
    while True:
        if formulario_temp["sexo"] not in 'MF':
                formulario_temp["sexo"] = str(input(f'Por favor, nos informe o Sexo valido [M/F]: ')).upper().strip()[0]
        else:
            break 
    resp = str(input('Deseja cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('Opção invalida!, Deseja cadastrar outra pessoa? [S/N] ')).upper().strip()[0]
        else:
            break
# guardar em um dicionario 
    lista_princ.append(formulario_temp.copy())
# guardar os dicionarios em uma lista
    formulario_temp.clear()
    if resp == 'N':
        break
# mostras quantas pessoas foram cadastradas
print(f'Ao todo temos {len(lista_princ)} pessoas cadastradas')
for l in range(0, len(lista_princ)):
    for k, v in lista_princ[l].items() :
        if k == 'idade':
            lista_idade.append(v)
        if k == 'sexo' and v == 'F':
            lista_fem.append(lista_princ[l]['nome'])
# a media de idade dessas pessoas
print(f'A média de idade é {sum(lista_idade) / len(lista_idade):.0f} anos')
# uma lista com as mulheres
print(f'As mulheres cadastradas foram {lista_fem}')
# uma lista de pessoa com idade acima da media 
print(f'Lista das pessoas que estão acima da média de todas as idades que é {sum(lista_idade) / len(lista_idade)}:')
for l in range(0, len(lista_princ)):
    for k, v in lista_princ[l].items():
        if k == 'idade':
            if v > (sum(lista_idade) / len(lista_idade)):
                print(f'Nome = {lista_princ[l]["nome"]}, Sexo = {lista_princ[l]["sexo"]}, Idade = {lista_princ[l]["idade"]}' )
print('<< ENCERRADO >>')