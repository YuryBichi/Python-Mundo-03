def leia_int(msg):
    while True:
        n1 = str(input(msg))
        try:
            valor = int(n1)
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um valor do tipo inteiro valido.\033[m')
            continue
        else:
            return valor
            break


def leia_real(msg):
   while True:
        n2 = str(input(msg))
        try:
            valor = float(n2)
        except (ValueError, TypeError):
            print('\033[0;34mERRO: Digite um valor de real válido.\033[m')
            continue    
        else:
            return valor
            break
    
