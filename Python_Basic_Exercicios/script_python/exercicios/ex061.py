termo = int(input('Qual termo deseja para PA: '))
razao = int(input('Digite a razão de sua PA: '))
num = 0
while termo != 0:
    print(num, end = ' ')
    num += razao
    termo -= 1