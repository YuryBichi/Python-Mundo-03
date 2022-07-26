from dados import *
from interface import *


if not arq_existe('jujuba.txt'):
    criar_arquivo('jujuba.txt')

while True:
    resp = abre_menu([
    'Ver pessoas cadastradas', 
    'Cadastrar nova pessoas', 
    'Sair do sistemas'
    ])
    if resp == 1:
        # Mostra lista de pessoas cadastradas
        ler_arquivo('jujuba.txt')
        sleep(1)

    elif resp == 2:
        # Cadastra uma nova pessoa
        titulo('novo cadastro')
        nome = str(input('Nome: ')).strip().title()
        idade = leia_int('Idade: ')
        criar_cadastro('jujuba.txt', nome, idade)
        sleep(1)

    elif resp == 3:
        # Sai do sistema
        titulo('saindo do sistema... até logo')
        break
    else:
        print('\033[;31mERRO: digite uma opção válida!\033[m')
        sleep(1)
    sleep(2)
