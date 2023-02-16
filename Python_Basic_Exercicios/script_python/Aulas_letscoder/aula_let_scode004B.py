#ciando uma FUNÇÂO

# função inicial
def saudacao(): # para criar uma função temos que colocar o de
    print('Seja Bem vindo')
    print('Ola, é um prazer ter você fazendo esse curso')

saudacao() # aqui estamos chamando a função que foi feita acima
#vantagem de um função é que pode ser usadas varias vezes sem repedir o codigo inteiro, somente colocando a função novamente 

# FUNÇÃO  com parametros 
nome = str(input('Digite seu nome: ')).title()
curso = str(input('Qual que esta fazendo: ')).title()
def saudacao(nome, curso): 
    print(f'Seja bem vindo {nome}!')
    print(f'é um prazer em ter você conosco neste curso de {curso}')
    
saudacao(nome, curso)

#FUNÇÃO com parametros default
def saudacao(nome, curso = 'Python'): #dessa forma, a variavel curso ja esta defenida que é python, então ao usar  a função não precisamos colocar nela o curso, somente o nome, porque o curso ja esta sendo definido que é python, mas ele é aberto a alteração, só colocar o nome do curso depois do nome, ai a variavel curso é alterada para o curso que for colocado 
    print(f'Seja bem vindo {nome}!')
    print(f'é um prazer em ter você conosco neste curso de {curso}')

saudacao('Luana') 

#FUNÇÂO com retorno
def soma(num1, num2):
    return num1 + num2 #esse comando faz retornar a soma das duas variaveis que estão dentro da função soma()
#IMPORTANTE, sempre que usamos a função return, a função para de funcionar, então se tivesse outra função dentro desse bloco da função soma(), não iria ser executado
resultado = soma(5, 4) #aqui a 5 esta representando o num1 e o 4 esta representando o num2
print(f'O resultado da soma é {resultado}')

print('-=-' * 20)
print('CALCULADORA AVANÇADA')
print('-=-' * 20)

def calculadora(num1, num2, operacao = '+'):
    if operacao == '+':
        return num1 + num2
    elif operacao == '-':
        return num1 - num2
    elif operacao == '*':
        return num1 * num2
    elif operacao == '/':
        return num1 / num2

resultado = calculadora(10, 20, '-')

print(resultado)