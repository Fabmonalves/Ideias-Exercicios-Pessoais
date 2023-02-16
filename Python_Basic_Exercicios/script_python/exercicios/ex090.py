ficha = {}
ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
if ficha['media'] >= 7:
    ficha['situacao'] = 'APROVADO'
elif 5 <= ficha['media'] > 7:
    ficha['situacao'] = 'RECUPERAÇÂO'
else:
    ficha['situacao'] = 'REPROVADO'
print('-=' *40)
for k, v in ficha.items():
    print(f'{k} é igual a {v}')