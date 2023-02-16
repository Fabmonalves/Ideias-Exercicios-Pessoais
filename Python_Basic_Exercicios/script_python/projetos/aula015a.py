from tkinter import N


while True: # colocando enquanto verdadeiro, faz o looping ficar infinito, só parando com a função break
    n = int(input('Digite um número: '))
    if n == 999:
        break # essa função faz parar o looping
    s = 0
    s += n
print(f'A soma vale {s}.')
