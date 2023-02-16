#variaveis compostas listas
teste = []
teste.append('Fabricio')
teste.append(26)
print(teste)
galera = []
galera.append(teste[:])
galera[0][0] = 'Luana'
galera[0][1] = 20 # essa lista esta dentro de outra lista, por isso os dois paramentros dentro de couchetes [], primeiro paramentro estou dizendo que é a primeira lista e o segundo paramentro eu percorro dentro dessa lista 
print(galera)

#ex usando o comando for e lista compostas

pessoas = [['Fabricio', 26], ['Luana', 20], ['Liriel', 18], ['Fernando', 22]]
for c in pessoas:
    print(f'{c[0]} tem {c[1]} anos de idade')
    
#ex usando input 
pessoas01 = []
dados = []
for c in range(0,3):
    dados.append(str(input('Nome: '))).title().strip()
    dados.append(int(input('Idade: ')))
    pessoas01.append(dados[:])
    dados.clear()
print(pessoas01)