#feita por mim
lista_num = []
lista_pares = []
lista_impares = []
for c in range(0,7):
    lista_num.append(int(input(f'Digite o {c + 1}° número: ')))
    if lista_num[c] % 2 == 0:
        lista_pares.append(lista_num[c])
        lista_pares.sort()
    else:
        lista_impares.append(lista_num[c])
        lista_impares.sort()
print(f'Os valores pares digitados foram: {lista_pares}') 
print(f'Os valores impares digitados foram: {lista_impares}')
print(lista_num)

#feita por mim
lista_par = []
lista_imp = []
princ = []
for c in range(0,7):
    num = int(input(f'Digite o {c + 1}° número: '))
    if num % 2 == 0:
        lista_par.append(num)
        lista_par.sort() 
    else:
        lista_imp.append(num)
        lista_imp.sort()
princ.append(lista_par[:])
princ.append(lista_imp[:])
print(f'Os valores pares digitados foram: {princ[0]}')
print(f'Os valores impares digitados foram: {princ[1]}')
print(princ)

#feita pelo professor
num = [[], []]
for c in range (0,7):
    valor = int(input(f'Digite o {c + 1}° valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
        num[0].sort()
    else:
        num[1].append(valor)
        num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')
print(num)