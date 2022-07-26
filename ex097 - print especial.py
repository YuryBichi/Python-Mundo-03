def escreva(msg):
    tam = len(msg) + 8
    print('~' * tam)
    print(f'    {msg}')
    print('~' * tam)


# Programa principal
escreva(str(input('Escreva o Titulo: ').upper()))