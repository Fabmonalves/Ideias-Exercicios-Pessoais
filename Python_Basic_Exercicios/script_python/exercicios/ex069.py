lista_maior = []
lista_m = []
lista_f_menor = []
while True:
    print('-' * 20)
    print('CADASTRE UAM PESSOA')
    print('-' * 20)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).upper().strip() [0]
    print('-' * 20)
    while sexo != 'MF':
        if sexo != 'M' and sexo != 'F':
            sexo = str(input('informe um Sexo valido: [M/F] ')).upper().strip() [0]
        else:
            break
    if idade >= 18:
        lista_maior.append(idade)
    if sexo == 'M':
        lista_m.append(sexo)
    if sexo == 'F' and idade < 20:
        lista_f_menor.append(sexo)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip() [0]
    while continuar != 'SN':
        if continuar != 'S' and continuar != 'N':
            continuar = str(input('Digitar uma opção valida, Quer continuar? [S/N] ')).upper().strip()[0]
        else:
            break
    if continuar == 'N':
        break
print('-' * 20)
print('FIM DO PROGRAMA')
print('-' * 20)
print(f'total de pessoas com mais de 18 anos: {len(lista_maior)}')
print(f'Ao tpdp temos {len(lista_m)} homens cadastrados.')
print(f'E temos {len(lista_f_menor)} mulheres com menos de 20 anos.')