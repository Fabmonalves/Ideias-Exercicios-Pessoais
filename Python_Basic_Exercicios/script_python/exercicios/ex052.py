numero = int(input('Digite um número: '))
ePrimo = 0

for i in range(1, (numero + 1 )):   # Nesse caso, será veiro a vistoria do 1 até o numero exato que foi colocado, o numero primo só é divisivel por 1 e por ele mesmo, então colocamos o ePrimo += 1 para calcular quantas vezes ele esta sendo divisivel, se o resultado for 2 então ele é primo, porque nesse calculo ele foi divisivel duas vezes , por 1 e por ele mesmo     
  if numero % i == 0:
    ePrimo += 1
    
if ePrimo  == 2 :
  print(f'O numero {numero} é primo')
else:
  print(f'O número {numero} nao é primo')
  
  #resolução do professor abaixo 
num = int(input('Digite um numero: '))
tot = 0
for c in range(1, num + 1):
  if num % c == 0:
    print('\033[33m', end = ' ')
    tot += 1
  else:
    print('\033[31m', end = ' ')
  print(f'{c}', end ='')
print(f' \033[mO número {num} foi divisivel po {tot} vezes')
if tot == 2:
  print('E por isso o numero é PRIMO')
else:
  print('E por isso o numero NÂO é PRIMO')