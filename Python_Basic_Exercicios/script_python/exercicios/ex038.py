n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print('O número {} é maior'.format(n1))
elif n2 > n1:
    print('O número {} é maior'.format(n2))
elif n1 == n2: 
    print('Não existe vamor maior, os dois numeros {} e {} são igauis'.format(n1 , n2))