soma = 0
cont = 0
for c in range(1, 7):
    numero = int(input(f'Digite o {c} valor: '))
    cont += 1
    if numero % 2 == 0:
        soma += numero
print(f'Você informou {cont} Numeros e a soma dos numeros PARES são {soma}')
