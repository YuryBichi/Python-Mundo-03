def leia_dinheiro(msg):
    while True:
        p = input(msg).strip().replace(',','.')
        if p.isspace() or p.isalpha():
            print(f'\033[0;31mERRO: "{p}" é um preço inválido!\033[m')
        
        elif p.isnumeric(): 
            p = float(p)
            return p
        else:
            print(f'\033[0;31mERRO: "{p}" é um preço inválido!\033[m')
