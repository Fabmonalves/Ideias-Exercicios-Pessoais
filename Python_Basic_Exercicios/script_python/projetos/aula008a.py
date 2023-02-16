import math # dessa forma eu estou importanto a biblioteca math inteira 
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('a raiz quadrada do {} é {:.2f}, raiz esta arredondada pra cima por conta do comando ceil da biblioteca math'.format(num, math.ceil(raiz))) #  pode ser feito dessa forma, esse ceil esta arredondando pra cima, a floor seria pra arredondar pra baixo, tem outros atalhos interessantes que pode ser usados dessa forma 

from math import sqrt, floor # dessa forma eu estou importanto apenas a função sqrt da biblioteca math 
num1 = int(input('Digite outro número: '))
raiz1 = sqrt(num1) #dessa forma, filtrando a função que deseja usar usando o from biblioteca import função, a gente só precisa defiir a função aqui e não precisa fazer igual o exemplo acima usando a biblioteca e a função 
print('A raiz quadrada do numero {} é {:.2f}'.format(num1, raiz1))

num2 =int(input('Digite outro número: '))
raiz2 = floor(num2) #dessa forma, filtrando a função que deseja usar usando o from biblioteca import função, a gente só precisa defiir a função aqui e não precisa fazer igual o exemplo acima usando a biblioteca e a função 
print('A raiz estando arredondada pra baixo fica {}, usando o comando'.format(raiz2))

# import + se apertar a tecla CTRL + espaço, a gent epode ver a lista de bibliotecas que eu posso colocar, biblioteca padrão que ja vem com o python
import emoji 
print(emoji.emojize("terminado :heart:", language = 'alias')) # esse comando inseri oemotion de um coração, foi pegado pelo site https://pypi.org/project/emoji/, foi isntalado essa biblioteca que não tinha, tem varias outras, para instalar, pegar no site pip e ver como usar ela la mesmo 