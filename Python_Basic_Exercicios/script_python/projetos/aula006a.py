n1 = input('Digite um numero: ')
print(type(n1)) # como não tem uma definição de valor nesse comando, o codigo entende como uma string por estar entre aspas 

n2 = int(input('Digite um numero para ser somado: '))
print(type(n2)) # nesse caso o codigo entende que o valor inserido dentro desse input será inteiro porque estamos dizendo no int() que tudo que estiver dentro dele será inteira

n4 = int(input('Digite um numero para ser somado: '))
print(type(n4))  # nesse caso o codigo entende que o valor inserido dentro desse input será inteiro porque estamos dizendo no int() que tudo que estiver dentro dele será inteira

n3 = float(input('Digite um numero : '))
print(type(n3)) # nesse caso  o codigo entende que tudo que vai dentro do float() será numero real

soma = n2 + n4

print(' A soma entre {} e {} vale {}'.format(n2, n4, soma)) # esse comando facilita muito, muito melhor q1ue usar a virgula para separar, ele funciona como uma especie de array mas em python, onde a ordem das variaveis dentro do .format pega a ordem das chaves dentro da string, dependendo do codigo, deixa a linha mais limpa e menor, se acostumar a usar esse formato, lembrando que esse formato só funciona apartir do python 3
