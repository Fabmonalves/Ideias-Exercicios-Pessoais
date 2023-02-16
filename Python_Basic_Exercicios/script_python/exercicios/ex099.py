from time import sleep
def maior(*num):
    print('-=' * 30)
    print('Analisnado os valores passados...')
    if len(num) > 0:
        for i in num:
            print(i, end = ' ', flush = True)
            sleep(0.5)
        print(f'foram informados {len(num)} valores ao todo.')
        sleep(0.5)
        print(f'O maior valor informado foi {max(num)}')
        sleep(0.5)
    else:
        sleep(0.5)
        print(f'Foram informados 0 valortes.')
        sleep(0.5)
        print('O maior valor informado foi 0.')
    

maior(2,9,4,5,6,8)
maior(2,8,4)
maior(1,2)
maior(4)
maior()