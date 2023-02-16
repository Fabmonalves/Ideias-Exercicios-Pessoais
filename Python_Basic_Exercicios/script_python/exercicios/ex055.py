lista_nomes = []
lista_pesos = []
for c in range(0, 2):
    nome = str(input('Digite seu nome: ')).title()
    lista_nomes.append(nome)
    peso = float(input('Digite seu peso: '))
    lista_pesos.append(peso) # Esse comando só pra guardar os pesos das pessoas mesmo das pessoas
   
print(f'O maior peso cadastrada é {max(lista_pesos)}Kg')
print(f'O menor peso cadastrado é {min(lista_pesos)}Kg')