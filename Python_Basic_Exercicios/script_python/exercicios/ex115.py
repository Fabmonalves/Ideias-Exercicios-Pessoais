from ex115p.lib.interface import *
from ex115p.lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver Pessoas cadastradas', 'Cadastrar pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Opção de listar o conteudo de um arquivo
        lerArquivo(arq)
        mensagem('Opção 1')
    elif resposta == 2:
        #opção de cadastro de uma pessoas para
        mensagem('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
        mensagem('Opção 2')
    elif resposta == 3:
        mensagem('Saindo do programa... até logo!')
        break
    else:
        print(f'\033[31mERRO! Digite um número inteiro válido.\033[m')
    sleep(2)
    