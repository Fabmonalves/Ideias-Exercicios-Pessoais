parar = 0
lista_num = []
while parar != 999:
    num = int(input('Digite um número [999 para parar]: '))
    parar = num
    if parar != 999:
        lista_num.append(num)
print(lista_num)
print(f'Voce digitou {len(lista_num)} números e a soma entre eles doi {sum(lista_num)}.')