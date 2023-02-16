termo = int(input('Qual termo deseja para PA: '))
razao = int(input('Digite a razão de sua PA: '))
num = 0
res = ''
while res != 'N':
    print(num, end = ' ')
    num += razao
    termo -= 1
    if termo == 0:
        res = str(input(' \n Fim da PA, deseza fazer com outros termos? [S/N]: ')).upper()
        if res != 'N':
            num = 0
            termo = int(input('Digite o novo termo que deseja: '))
            inicio = int(input('Digite o inicio para a PA: '))
            razao = int(input('Digite a razão de sua PA: '))
        else:
            print('Fim do programa')
        
        
    