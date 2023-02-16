import random
print('-=-' * 20)
print('Adivinhe um Número')
print('-=-' * 20)

pc = random.randint(0,10)
escolha = int(input('Adivinhe o Número que pensei: '))
chute = 1
while escolha != pc:
    if escolha < pc:
        escolha = int(input('número errado, tente novamente com um numero maior: '))
        chute += 1
    elif escolha > pc:
        escolha = int(input('número errado, tente novamente com um numero menor: '))
        chute += 1
print(f'Parabens, foram {chute} chutes para acertar')
