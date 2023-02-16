from time import sleep
def contador(a, b, c):
    while True:
        if c == 0:
            c += 1
        if a < 0:
            a *= -1
        else:  
            if a < b:
                print(f'Contagem de {a} até {b} de {c} em  {c}')
                sleep(1)
                for i in range(a, b + 1, c):
                    print(i, end = ' ', flush = True)
                    sleep(0.5)
                print('FIM!')
                print('-='*30)
                break
            if a > b and c > 0:
                print(f'Contagem de {a} até {b} de {c} em {c}')
                sleep(1)
                for i in range(a, (b - 1), -c):
                    print(i, end =' ', flush = True)
                    sleep(0.5)
                print('FIM!')
                print('-='*30)
                break
            if a > b and c < 0:
                print(f'Contagem de {a} até {b} de {c} em {c}')
                sleep(1)
                for i in range(a, (b + 1), c):
                    print(i, end = ' ', flush = True)
                    sleep(0.5)
                print('FIM!')
                print('-='*30)
                break
            
        
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Salto: '))
print('-='*30)
contador(inicio, fim, passo)