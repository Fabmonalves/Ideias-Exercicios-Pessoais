frase = str('Ola, meu nome é Fabricio e estou aprendendo a programar em python, essa aula é sobre manipulação de Texto')
# importante!, essa string acima, na memoria do PC , cada palavra e espaço comporta um espaço na memoria, começando de 0 até o fim dela, no caso de cima, o 'O' esta na colocação 0 da memoria 
print('##############################')
print('--------- Fatiamento ---------') 
print('##############################')

print(frase[9], 'fatiamento, estamos filtrando o caractere da 9° colocação dentro da variavel "frase"'.format(frase[9])) # nesse caso será filtrado a palavra na 9° colocação do texto dentro da variavel frase 
print('-----||-----')
print(frase[9:19], '-fatiamento, estamos filtrando o caractera da 9° colocação até a 19° colocação') # nese caso quando colocamos esses parametros dentro do colchete, estamos dizendo para o programa pegar a letra na colocação 9 até a colocação 19, mas a letra da colocação 19 será desconsiderada, considera a colocação antes dele, que nesse caso é a 18, se a gente usar o paramentro [:19] nesse exemplo, então começa da colocação 0 até a 19, quando não colocamos valores nos parametros nesse exemplo, ele recebe valor zero, o mesmo vale para o exemplo [9:], o sistema entende que nesse caso, o segundo parametro, vai ser o valor maximo disponivel dentro da frase, então iria da colocação 9 até o final 
print('-----||-----')
print(frase[0:31:3], '-fatiamento, estamos filtrando os caracteres da 0° colocação até a 31° mas pulando de dois em dois') # nesse caso a situação é a mesma, mas com uma diferença, esse terceiro parametro dentro dos colchetes, de valor 3 esta dizendo para fazer a filtragem dos valores de 9 à 19 pulando de dois em dois, nesse exemplo, se não sabe o valor da colocação do ultimo caracter da frase, pode ser feito dessa forma [0::3], se não colocarmos nada no parametro do ultimo caracter, então ele vai pegar todos os caracter da frase, do começo do paramentro que foi informado até o fim e pulando 
print('-----||-----')

print('##############################')
print('---------- Análise -----------') 
print('##############################')

print(len(frase), 'caracteres dentro da variavel "frase"')  # esse comando vai contar os caracteres que contem dentro da variavel frase
print('-----||-----')
print(frase.count('o'), 'letras "o" na frase')  # esse comando conta quantos vezes o caractere 'o' aparece na frase
print('-----||-----')
print(frase.count('o', 0, 75), 'letras, temos {} letras "o" com fatiamento, pegando até a locação 75 dentro da variavel frase'.format(frase.count('o', 0, 75))) # nesse caso a gente esta filtrando as letras "o" dentro da variavel, mas com um fatiamento, começando da colocação 0 até a 75
print('-----||-----')
print(frase.find('Fab'),'° posição da memória, onde começou') #Esse comando filtra e me diz a localização dentro da memoria, o momento que começou, caso não tenha nenhuma ele me responde com -1
print('-----||-----')
print('Fabricio' in frase,', tem a palavra na frase') # esse comando esta perguntando se tem a palavra "Fabricio" na frase que esta dentro da string, ele responde com true ou false
print('-----||-----')

print('##############################')
print('------- Transformação --------') 
print('##############################')

print(frase.replace('Fabricio', 'Luana')) # ese comando faz alteração, o primeiro parametro vai filtrar e o segundo é o que vai ser substituido 
print('-----||-----')
print(frase.capitalize()) # esse comando capitalize faz com que o primeiro caractere fique em caixa auta(maiuscula) enquanto os demais ficam em minusculas 
print('-----||-----')
print(frase.upper()) # esse comando faz com que todos os caracteres fiquem em maiuscula(caixa auta)
print('-----||-----')
print(frase.lower()) # esse comando faz com que todos os caracteres fiquem em minusculas
print('-----||-----')
print(frase.title()) # esse comando é parecido com o comando capitalize, mas direfente dele, ele coloca a primeira letra maiuscula daca frase
print('-----||-----')
print(frase.strip()) # ese comando vai tirar todos os espaços inuteis da grase, espaços esses que ficam no começo e no fim da frase, bem util para formularios 
print('-----||-----')
print(frase.rstrip()) # esse comando é o mesmo de cima, a direfença é o 'r' right, que faz com que sómente os espaços exedentes da direita sejam remobidos 
print('-----||-----')
print(frase.lstrip()) # esse comando é o mesmo de cima, a direfença é o 'l' light, que faz com que sómente os espaços exedentes da esquerda sejam remobidos 
print('-----||-----')

print('##############################')
print('------- Divisão/Junçaõ -------') 
print('##############################')

print(frase.split()) # faz com que as palavras sejam divididas entre os espaços uma das outras, e cada palavra fica com uma nova indexação, em uma lugar diferente da memoria, então cada palavra fica na posição 0 dentro de sau lista 
print('-----||-----')
print('-'.join(frase)) # de forma analoga ao split, esse comando faz a junção das palavras, junta com o que estiver dentro da string dela 
print('-----||-----')

print('##############################')
print('--------- Curiosidade --------') 
print('##############################')

print(''' Quando estamos diitando um texto que 
vai mais de uam linha e tu quer preservar 
esses espaços que faz, pulando linhas, pode 
colocar o texto dentro de três aspas que funciona ''')
