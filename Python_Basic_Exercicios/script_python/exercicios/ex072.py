numero_tupla = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite um número entre 0 a 20: '))
while True:
    if num >= 0 and num <= 20:
        break
    else:
        num = int(input('Zente novamente, Digite um número entre 0 a 20: '))        
print(f'Você digitou o numero {numero_tupla[num]}.')
print('fim do programa')