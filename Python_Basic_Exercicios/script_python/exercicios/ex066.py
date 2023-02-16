lista_num = []
while True:
    num = int(input('Digite um número (999 para parar): '))
    if num != 999: #se num for diferente de 999 faça
        lista_num.append(num) #adicione o num a lista
    else: #senão 
        break #pare o looping
print(f'Foram digitados {len(lista_num)} números e a soma entre eles é {sum(lista_num)}.')