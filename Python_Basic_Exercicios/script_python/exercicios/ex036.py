from time import sleep
print('-=-' * 20)
print('\033[32mSimule aqui seu empréstimo bancário!\033[m')
print('-=-' * 20)

casa = float(input('Digite aqui o valor da Casa desejada: '))
salario = float(input('Agora me informe o valor de seu salario: '))
anos = int(input('Em quantos anos deseja fazer a simulação? '))
print('Processando...')
sleep(1)
print ('''A casa que deseja comprar vale R${:.2f}
seu salario é de R${:.2f} 
E pretende pagar em {} anos...'''.format(casa, salario, anos))
print('Entendi, me de um tempo para calcular as condições pra ti...')
sleep(1)
parcela = casa / (anos * 12)
parcela_teto = salario * 30 / 100

if parcela < parcela_teto: 
    print('A parcela fica R$\033[32m{:.2f}\033[m, dentro da simulação com "0%" de juros \n Você pode fazer esse emprestimo dentro dessas condições'.format(parcela))
else:
    print('Infelizmente a parcela R$\033[31m{:.2f}\033[m exede "30%" de sua renda, mesmo com a taxa de juros sendo "0%" \n Dentro dessas condições não pode pegar o Empréstimo'.format(parcela))
print('Fim da simulação')
