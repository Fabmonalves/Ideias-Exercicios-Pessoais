def area(a, b):
    s = a * b
    print(f'A área de um terreno {a:.2f}x{b:.2f} é de {s:.2f}m² ')


print('Controle de Terrenos')
print('-' * 20)
a = float(input('Largura (m): '))
b = float(input('Autura (m): '))
area(a, b)