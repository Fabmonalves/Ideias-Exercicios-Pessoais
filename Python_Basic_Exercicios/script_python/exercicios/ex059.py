import numpy
from time import sleep
lista = []
for c in range(1,3):
    escolha = int(input(f'Digite o {c}° número: '))
    lista.append(escolha)
print('''[0]mostrar lista
[1]somar
[2]multiplicar
[3]maior
[4]novos numeros
[5]sair do programa''')
opcao = int(input('Escolha uma das opções acima: '))
while  opcao != 5:
    if opcao == 0:
        print(lista)
        opcao = int(input('Escolha outra opção:'))
    elif opcao == 1:
        print(f'A soma dos valores é {sum(lista)}')
        opcao = int(input('Escolha outra opção: '))
    elif opcao == 2:
        print(f'A multiplicação dos valores é {numpy.prod(lista)}')
        opcao = int(input('Escolha outra opção: '))
    elif opcao == 3:
        print(f'O maior número adicionado na lista é {max(lista)}')
        opcao = int(input('Escolha outra opção: '))
    elif opcao == 4:
        lista.append(int(input('Digite o número que deseja incluir a lista: ')))
        opcao = int(input(f'Número adicionado, agora escolha outra opção: '))
    elif opcao == 5: 
        print(f'Opção {opcao} selecionada, saindo do programa...')   
    else:
        print('Opção invalida, favor, selecionar uma opção valida!') 
        opcao = int(input('Escolha outra opção: '))
sleep(1)
print('Fim do programa')