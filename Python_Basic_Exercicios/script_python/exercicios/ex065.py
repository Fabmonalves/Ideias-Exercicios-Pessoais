continuar = ''
lista_num = []
while continuar != 'N':
    num = float(input('Digite um número: '))
    lista_num.append(num)
    continuar = str(input('Deseja continuar? [S/N]: ')).upper().strip() [0]
    if continuar != 'S' and continuar != 'N':
        print('opção invalida, por favor, me informar um valor valido!')
        continuar = str(input('DESEJA continuar? [S/N]: ')).upper().strip() [0]
print(f'Você digitou {len(lista_num)} númeos e a média foi {sum(lista_num) / len(lista_num)}')
print(f'O maior valor foi {max(lista_num):.0f} e o menor foi {min(lista_num):.0f}')