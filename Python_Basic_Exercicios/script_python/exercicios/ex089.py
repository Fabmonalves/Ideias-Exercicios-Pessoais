princ = []
temp = []
while True:
    temp.append(str(input('Nome: ')).strip().title())
    for c in range(1,3):
        temp.append(float(input(f'Nota {c}°: ')))
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Deseja continuar? [S/N]: ')).title().strip()[0]
    while True:
        if resp not in 'SN':
            resp = str(input('Deseja continuar? [S/N]: ')).title().strip()[0]
        else:
            break
    if resp == 'N':
        break
print('-=' * 30)
print(f'{"No.":<4} {"NOME":<20} {"MÉDIA"}')
print('-' * 35)
media = 0
for c in range(0, len(princ)):
    media = (princ[c][1] + princ[c][2]) / 2
    print(f'{c:<4} {princ[c][0]:<20} {media}')
print('-' * 35)
while True:
    aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if aluno <= len(princ) -1:
        print(f'As notas de {princ[aluno][0]} foram {princ[aluno][1], princ[aluno][2]}') 
    if aluno == 999:
        break
print('Fim do programa...')