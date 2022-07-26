def area(larg, comp):
    a = larg * comp
    print(f'-> A área de {larg}x{comp} é {a}m².')

def escreva(msg):
    tam = len(msg) + 8
    print('~' * tam)
    print(f'    {msg}')
    print('~' * tam)


# Programa principal
escreva('>> CALCULO DE ÁREA <<')
l = float(input('- LARGURA: '))
c = float(input('- ALTURA: '))
area(l, c)
