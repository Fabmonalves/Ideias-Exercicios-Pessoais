num = int(input('Digite um termo: '))
t1 = 0
t2 = 1
cont = 3
print(f'{t1} -> {t2}', end = ' -> ')
while cont <= num:
    t3 = t1 + t2
    print(f'{t3}', end = ' -> ')
    t1 = t2
    t2 = t3
    cont += 1
    
print(' FIM')