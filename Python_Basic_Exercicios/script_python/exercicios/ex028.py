import random
import time
print('-=-' * 20)
print('''Ola, vamos jogar?
Vamos jogas assim, eu vou pensar e um numero e você tenta acerter ok?
pra facilitar, eu vou pensar em um número de 1 à 5''')
print('-=-' * 20)
print ('\033[32mPensando em um numero...\033[m')
time.sleep(2) # essa função da um time  para prosseguir 
numero = random.randint(0, 5)
print('Pronto, Adivinhe o numero que pensei!')
escolha = int(input('Chute um número: '))

if escolha == numero:
    print('Nossa, você é bom hein, \033[32;40macertou!\033[m o numero que pensei foi {} mesmo'.format(numero))
else:
    print('hahaha, não foi esse número que pensei não viu, pensei no \033[31m{}\033[m'.format(numero))
    print('tente novamente, Chute outro numero!')
print('Uma pena, mas não aprendi ainda a como te dar outra cance, me reset se quiser tentar novamente!')

