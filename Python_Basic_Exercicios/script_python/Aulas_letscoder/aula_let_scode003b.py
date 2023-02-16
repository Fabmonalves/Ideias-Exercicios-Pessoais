lista = [1, 2, 3, 5, 10, 25, 5, 4] # toda lista é dentro de colchetes [] no python 

# Adicionando um elemento no final da lista com appended
print(f'Antes do append: {lista}')
lista.append(3) #adicionando o valor 3 no final da lista
print(f'Depois do append{lista}') 

# Adicionando um novo valor na lista mas dessa vez escolhendo a posição do mesmo usando insert
lista.insert(4, 32) # o primeiro parametro definimos o local onde ela vai ser inserida e o segundo parametro é o valor inserido
print(f'Depois do insert {lista}')

# Juntando otra lista usando o comando extend
lista2 = [2, 4, 6] 
lista.extend(lista2) #esse comando vai adicionar a lista2 no final da lista
print(f'Depois de ter adicionado a lista2 na lista usando o comando extend {lista}')

# Removendo um item da lista usando pop
lista.pop() #se não colocarmos parametros, ele vai tirar o ultimo item da lista, caso colocarmos o parametro, ele vai tirar de aconrdo com o mesmo, seguindo a ordem dos itens, exemplo, se o parametro for 4m tiraremos o item da 4° colocação da lista
print(f'Depois de ter usado o comando pop {lista}')
lista.pop(4)
print(f'Lista depois de tirarmos o item da 4° colocação usando pop {lista}')

# Removendo usando o comando remove
lista.remove(3) # Esse comando vai remover o item que tem valor 3, no nosso caso, temos mais de um 3 na lista, então ele vai pegar o primeiro 3 da esquierda pra direita e remover ele 
print(f'Depois do comando remove {lista}')

# Metodo de contagem com o count
print(f'Quantidade de 2 na lista {lista.count(2)}')

#comando para dizer o indice do item dentro da lista, locação da lista
print(f'Qual o indice do elemento 5 dentro da lista: {lista.index(5)}°') # Esse comando vai me informar o indice do primeiro item da lista da esquerda pra direita 

# Comando para ordenar a lista com sort
lista.sort() # Esse comando ordena a lista de forma crescente
print(f'Lista depois do comando sort {lista}')
lista.sort(reverse = True)
print(f'Lista de ordem decrescente usando o comando com o parametro, sort(reverse = Ture) {lista}')

#FUNÇÕES PARA LISTA

# QUANTIDADE DE ELEMENTROS DA LISTA COM A FUNÇÃO len
print(f'Quantidade de elementos da lista com o len {len(lista)}') 

#FAZENDO A SOMA DOS ELEMENTROS DA LISTA USANDO A FUNÇÃO sum
print(f'Somando os elementros com a função sun {sum(lista)}')

# RETORNANDO O MAIOR VALOR DA LISTA USANDO A FUNÇÃO max
print(f'O maior valor da lista usando o comando max é {max(lista)}')
#RETORNANDO O MENOR VALOR DA LISTA USANDO A FUNÇÃO min
print(f'O menor valor da lista usando o comando min é {min(lista)}')