def leiaInt(msg):
    valor = 0
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            valor = int(n)
            break
        else:
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    return valor
    
        
    


n = leiaInt('Digite um numero: ')
print(f'Você acabou de digitar o número {n}')