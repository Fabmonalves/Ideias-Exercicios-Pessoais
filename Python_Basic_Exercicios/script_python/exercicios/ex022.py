n_completo = str(input('Digite seu nome completo: '))
quantidade = len(n_completo.replace(' ','')) # esse comando esta dizendo para atrimuir para variavel esse comando , dizendo para contar os caracteres , comando usado com o len, e dentro do len, estamos dizendo para substituir os espaços com o comando .replace,  ' ' com nada '', sem espaço e nada, assim , na contagem ele vai desconsiderar os espaços 
separados = n_completo.strip().split() #Nesse comando estou tirando os eventuais espaços que a pessoa possa colocar antes ou depois do nome na digitação e com o comando split estou separando os nomes pelo espaço, para cada palavra esteja em uma lugar especifico da memoria, separados 
print('O nome completo em maiuscula é: {}'.format(n_completo.upper())) #Nome em maiuscula
print('O nome completo em minuscula é: {}'.format(n_completo.lower())) #Nome em minuscula
print('O nome {} contem {} caracteres sem considerar os espaços entre elas'.format(n_completo, quantidade))  #Comando esta contando os caracteres do nome desconsiderando os espaços 
print('O seu primeiro nome é {}, e esse nome contem {} caracteres'.format(separados[0], len(separados[0])))  #Nesse comando eu estou separando o primeiro nome quando eu coloco o parametro de fatiamento [0] e com o comando len eu estou pedindo para contar os caracteres que tem


