for c in range(1, 10):
    print(c, end = ' ')
print('Fim usando o comando for')

i = 1
while i < 10:
    print(i, end =' ')
    i += 1
print('Fim usando o comando while')

r ='S' #ESSA VARIAVEL IMPEDE DE ACONTECER DO COMANDO WHILE ENTRE EM LOOPING INFINITO caso esqueca de colocar para o usuario se deseja continuar dentro desse exemplo
while r == 'S': #aqui estamos dizendo que enquanto o r não receber o S faça, e na função perguntamos se quer continuar e colocamos a variavel r para o usuario alterar para entrar ou sair da condição
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]: ')).upper()
print('Fim do comando simplificado do while, esse tipo de comando não da pra fazer com o for')

#exemplo de while
num = 1
par = impar = 0 #podemos declarar variavel dessa forma também
while num != 0:
    num = int(input('Digite um número: '))
    if num != 0: #esse comando é para o while não considerar o valor 0 como valor par 
        if num % 2 == 0:
            par += 1
        else:
            impar += 1
print(f'Você digitou {par} números pares e {impar} números impares')