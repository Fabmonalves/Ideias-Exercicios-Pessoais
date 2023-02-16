s = str(input('Informe seu sexo [F/M]: ')).upper().strip() [0]#declarado uma variavel em fomato de string vazia 

while s not in 'MF': # se le, enqaunto sexo não tiver MF faça, uma forma simplificada e bem util
    s = str(input('Dados invalidos, por favor, Informe o sexo [F/M]: ')).upper().strip() [0] #esse 0 faz pegar apenas o primeiro caractere, caso a pessoa coloque por extenso o sexo
print(f'Sexo {s} cadastrado com sucesso')