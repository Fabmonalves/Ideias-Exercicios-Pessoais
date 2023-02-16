'''faça um programa que sorteie um numero, e que ele repita até o numero seja sorteado pelo programa usando a estrutura while'''

# codigo de repetição simples ----------------------------------------------------
import random
computador = random.randint(0,5) #aqui o computador ou programa vai escolher aleatoriamente um numero de 0 a 5 
usuario = int(input('Digite um numero etnre 0 e 5: '))
while usuario != computador:
    usuario = int(input('Numero errado, me informe outro número: '))
print('Você acertou, o número foi {} mesmo'.format(computador))
# FIM codigo de repetição simples ------------------------------------------------

# exemplo de estrutura de repetição continua -------------------------------------
print('Taduada')
contador = 0
tabuada = int(input('Digite o valor da tabuada: '))
while contador != 11: # da pra usar a estrutura while nesse caso, mas o mais indicado é usar a estrutura FOR 
    print('{} x {} = {}'.format(contador, tabuada, contador * tabuada))
    contador = contador + 1
# FIM exemplo de estrutura de repetição continua ---------------------------------



