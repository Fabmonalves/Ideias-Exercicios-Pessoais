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


def linha(tam=42):
    print('-' * tam)
    
    
def mensagem(msg):
    linha()
    print(msg.center(42))
    linha()
    
    
def menu(lista):
    mensagem('MENU PRINCIPAL')
    c = 1
    for item in lista: 
        print(f'{c} - {item}')
        c += 1
    linha()
    opc = leiaInt('Sua opção: ')
    return opc