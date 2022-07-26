def leia_int(msg):
    inteiro = False
    valor = 0

    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            inteiro = True
        else:
            print('\033[0;31m   ERRO! Digite um número válido.\033[m')
        if inteiro:
            break
    return valor

#Programa principal
n = leia_int('Digite um número inteiro: ')
print(f'Você digitou o número {n} !')