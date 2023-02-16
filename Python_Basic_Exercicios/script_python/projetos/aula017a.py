#listas []
num = [15, 2, 8, 8, 7, 9, 8]
print(num)
num[2] = 5 #Comando para alterar um elemento da lista
print(f'Depois de ter alterado o elemente da seguda posição da lista {num}' )
num.append(85) #colocando mais um elemento no fim da lista
print(f'Depois de ter acrescentado o novo valor no fim da lista {num}')
num.insert(0, 45) #comando para incluir um elemento dentro da lista, no começo 
print(f'Depois de ter acrescentado o novo valor dentro da colocação do parameentro, nesse exemplo, colocamos na colocaçaõ 0 da lista {num}')
num.sort()
print(f'Depois de colocar a lista em ordem usando o comando sort() {num}')
num.sort(reverse = True)
print(f'Depois de fazer a lista ficar em ordem de traz pra frente usando o paramentro reverse=True dentro de sort {num}')
num.remove(8)
print(f'Depois de usar o comando remove para remover o valor dentro do paramentro, lembrando que se tiver outro igual, ele remove o primeiro que encontrar {num}')
print(f'Essa lista tem {len(num)} elementos')
for c, v in enumerate(num): #a  variavel c nesse caso recebe o enumerate()
    print(f'Na posição {c}° encontrei o valor {v:>3}...')
    