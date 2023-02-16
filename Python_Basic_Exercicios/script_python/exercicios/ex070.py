lista_compras = []
lista_1000 = []
while True:
    nome = str(input('Nome do produto: ')).title().strip()
    preco = float(input('Digite o valor: '))
    lista_compras.append(preco)
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar != 'SN':
        if continuar != 'S' and continuar != 'N':
            continuar = str(input('Por favor, informar uma opção valida [S/N] ')).upper().strip()[0]
        else:
            break
    if preco > 1000.00:
        lista_1000.append(preco)
    if preco == min(lista_compras):
        produto_menor = nome
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'O total da compra foi R${sum(lista_compras):.2f}')
print(f'Temos {len(lista_1000)} produtos que custaram mais mais de R$1000.00')
print(f'O  produto mais barato foi {produto_menor} que custa {min(lista_compras)}') 