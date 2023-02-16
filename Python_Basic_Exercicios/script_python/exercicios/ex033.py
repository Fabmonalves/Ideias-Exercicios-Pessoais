n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input(' Digite o terceiro número: '))
if n1 > n2 and n1 > n3 and n3 < n2:
    print('O número {} é o maior'.format(n1))
    print('O número {} é o menor'.format(n3))
elif n2 > n1 and n2 > n3 and n1 < n3:
    print('O número {} é o maior'.format(n2))
    print('O número {} é o menor'.format(n1))
elif n3 > n1 and n3 > n2 and n2 < n1:
    print('O número {} é o maior'.format(n3))
    print('O número {} é o menor'.format(n2))

print('---FIN---')