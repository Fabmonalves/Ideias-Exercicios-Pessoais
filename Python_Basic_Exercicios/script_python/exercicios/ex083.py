expressao = str(input('digite uma expressão: '))
cont = 0
for c in expressao:
    if c == '(':
        cont += 1 
    elif c == ')':
        cont -= 1
if cont == 0:
    print('A expressão é valida')
else:
    print('A expressão é invalida!')
