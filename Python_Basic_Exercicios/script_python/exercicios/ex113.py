def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue # ese comando faz com que entre no laço novamente 
        except (KeyboardInterrupt):
            print(f'\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
            continue # ese comando faz com que entre no laço novamente 
        except (KeyboardInterrupt):
            print(f'\033[31mUsuario preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n 
   
    
        
    


num = leiaInt('Digite um numero: ')
real = leiaFloat('Digite um número Real: ')
print(f'Você acabou de digitar o número {num} e o real foi {real}')