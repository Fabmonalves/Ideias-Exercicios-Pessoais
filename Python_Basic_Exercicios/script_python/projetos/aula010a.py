#condições
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <= 3:
    print('Carro novo')
else:
    print('Carro velho')
print('---FIM---')

#condição simplificada 
tempo2 = int(input('Quantos anos tem sua moto? '))
print('Moto nova' if tempo2 <= 3 else 'Moto velha') #forma simplificada mas não muito usada por confundir o if e else, mas é uma formar de manter o codigo menor e simplificado 
print('---FIM---')

#aula10 pratica com exemplos
nome = str(input('Qual o seu nome? ')).title().strip() # colocando como title pra sair bonito caso a pessoa coloque o nome completo
if nome == 'Fabricio' or 'Fabricio' in nome: # aui é pra caso tenha Fabricio no nome, por isso a condição or
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia! {}'.format(nome))
print ('---FIN---')

p_nota= float(input('Digite sua nota de Português: '))
m_nota = float(input('Digite sua nota de Matemática: '))
media = (p_nota + m_nota) /2
if media >= 7:
    print('Parabéns, sua média foi {:.1f}; você passou! '.format(media))
else: 
    print('Faça a prova novamente, sua média foi {:.1f}; infelizmente não alçancou a média necessária pra passar :/ '.format(media))
print('---FIM---')

