from time import sleep


cores = [
    '\033[m', #Sem cor [0]
    '\033[;41m', #Vermelho [1]
    '\033[;42m', #Verde [2]
    '\033[;43m', #Amarelo [3]
    '\033[;44m', #Azul [4]
    '\033[;45m'] #Roxo [5]

def titulo(msg, cor=0):
    tam = len(msg) + 8
    
    print(f'{cores[cor]}')
    print('~'*tam)
    print(f'    {msg}'.upper())
    print('~'*tam)
    print(f'{cores[0]}')

def ajuda(com):
    help(com)

#Programa principal
while True:
    titulo('sistema de ajuda pyhelp.', 4)
    comando = str(input('-> Função ou biblioteca: '.strip().lower()))
    if comando in 'FIM':
        titulo('programa encerrado.', 1)
        break
    else: 
        titulo(f'acessando o manual de {comando}', 2)
        sleep(1)
        ajuda(comando)
