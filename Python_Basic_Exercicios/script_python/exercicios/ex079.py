lista_num = []
while True:
    num = (int(input('Digite um valor: ')))
    if num in lista_num:
        print('Valor duplicado! Não vou adicionar...')
    else:
        lista_num.append(num)
        lista_num.sort()
        print('Valor adicionado com sucesso...')
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar != 'SN':
        if continuar != 'S' and continuar != 'N':
            continuar = str(input('Digite uma opção valida, deseja continuar? [S/N] ')).upper().strip()
        else:
            break
    if continuar == 'N':
        break
print(f'Você digitou os valores {lista_num}')