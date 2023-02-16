f = str(input('Digite uma frase: ')).strip()
frase = f.replace(' ', '').upper()
frase_invertida = ''.join(reversed(frase)) #Esse comando faz com que a string seja invertida
if frase == frase_invertida:
    print(f'A frase {f} \033[32mé um Palindromo\033[m')
else:
    print(f'A frase {f} \033[31mnão é um Palindromo\033[m')
