print('Tabuada')
tabuada = int(input('Digite o numero da Tabuada desejada: '))
# esse exempplo de for é com dois paramentros ------------------------------
for variavel in range(0 , 11): # para variavel dentro do range(11) 'esse range esta defionindo a faixa, será de 0 a 10 porque coloquei valor 11, para se repetir 11 vezes, esta com dois parametros, 0 significa que vai começar do 0 e 11 significa que vai terminar até completar 11 vezes a ação 
    print('{} x {} = {}'.format(variavel, tabuada, variavel * tabuada))
# FIM do exempplo de for é com dois paramentros ----------------------------

# exemplo de for com três parametros ---------------------------------------
for numeros in range(0, 11, 2): # aqui estamos dizendo no range, que vai começar do zero, terminar na contagem 11 e pulando de 2 em 2, esse é o memso  conceito de fatiamento
    print(numeros)
#FIM do exemplo de for com três parametros ---------------------------------

# exemplo pratico do for ---------------------------------------------------
soma = 0
for i in range(1, 4):
    nota = float(input(f'Digite aqui sua nota {i}: ')) # se usarmos um f antes da string, então podemos simplesmente colocar a variavel dentro dos {}, é uam forma simplificada de usar o .format, bem mais pratico!!!!!
    soma = soma + nota
print(f'sua média é {soma / 3 :.2f}')

# FIM do exemplo pratico do for --------------------------------------------