# DICIONÁRIOS

#Criando dicionários

dicionario = {} #formas de criar m dicionario
dicionarios = dict() #formas de criar m dicionario

dicionario = {'nome':'Fabricio', 'idade':'26', 'altura':'1.81'} #formas de criar m dicionario 

print(dicionario)
print(dicionario['altura']) #dessa forma que acessamos os conteudos do dicionario, com a chave 

# Adicionando elementos em um dicionário

dicionario['programador'] = True  #Essa é a forma que adicionamos conteudos no dicionario
print(dicionario)

dicionario['altura'] = 2.00 # Esse comando vai sobrescrever o valor da altura no dicionario, porque a latura ja existe no mesmo 
print(dicionario)

# Iterando sobre um dicionário

for chave in dicionario: # esse comando faz com que percorra todas as chaves do dicionario 
    print(chave, dicionario[chave]) # incluindo esse comando dicionario[chave] eu estou dizendo para percorrer ao valor que esta contido na chave 
    
#Testando a existencia de uma chave
    
print('peso' in dicionario) #se le ' a chave peso esta dentro do dicionario?' dessa forma , se o resultado for true, significa que tem esa chave no dicionario, caso o resultado seja false, então não existe 
