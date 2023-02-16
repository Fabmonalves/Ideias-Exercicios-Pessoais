import math
numero = float(input('Digite m valor: '))
print(' O valor digitado foi {} e sua porção inteira é de {}'.format(numero, math.floor(numero))) # a função floor aredonda pra baixo, resolve nese caso tbm

numero2 = float(input(' Digite outro numero: '))
print(' O valor digitado foi {} e sua porção inteira é de {}'.format(numero2, math.trunc(numero2))) # a função trunc é a mais ideia nesse caso por que ela trava o numero inteiro 

from math import trunc, floor # importando desse jeito a gente usa apenas as duas funções , facilita se a gente for usar somente elas no codigo, deixa mais leve 

numero3 = float(input('Digite m valor: '))
print(' O valor digitado foi {} e sua porção inteira é de {}'.format(numero3, floor(numero))) # a função floor aredonda pra baixo, resolve nese caso tbm

numero4 = float(input(' Digite outro numero: '))
print(' O valor digitado foi {} e sua porção inteira é de {}'.format(numero4, trunc(numero2))) # a função trunc é a mais ideia nesse caso por que ela trava o numero inteiro 